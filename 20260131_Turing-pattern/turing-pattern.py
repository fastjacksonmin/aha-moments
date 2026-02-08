import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap

# Prefer GPU via CuPy when CUDA is available; fallback to NumPy otherwise
def _get_backend():
    # try:
    import cupy as cp
    # Actually use CUDA (fails if CUDA_PATH missing or nvrtc/cudart DLLs not found)
    cp.ones((1, 1))
    return cp, True
    # except Exception:
    #     return np, False

xp, _GPU = _get_backend()

# ==========================================
# 1. 模拟参数设置 (调节旋钮)
# ==========================================
# 网格尺寸
N = 500              

# 扩散系数 (Diffusivity)
# Dv 必须显著小于 Du 才能产生稳定的图灵模式
Du, Dv = 0.16, 0.08  # 扩散率保持 2:1，系统更稳定

# 反应参数 (F 和 k 是大自然的“旋钮”)
# 尝试以下组合:
# 斑点 (Spots): F=0.030, k=0.062
# 斑马纹 (Stripes): F=0.042, k=0.060
# 迷宫 (Maze): F=0.035, k=0.060
# 细胞分裂 (Mitosis): F=0.036, k=0.064
F, k = 0.035, 0.060  # 迷宫
F, k = 0.04, 0.060  # 反色迷宫
# F, k = 0.035, 0.062  # 条纹和斑点
# F, k = 0.035, 0.058  # 反色条纹
# F, k = 0.036, 0.058  # 反色条纹和斑点
# F, k = 0.034, 0.056  # 
F, k= 0.036, 0.064 # 细胞分裂 Mitosis

# Du, Dv = 0.16, 0.04  # 强制让扩散率比例达到 4:1 (关键！)
# F, k = 0.025, 0.05  # 降低 F 和 k，让斑块有空间“长大”

dt = 1            # 时间步长


cmap = 'magma'
# Color map for Cheetah
# custom_colors = ['#D7AC65', '#211309']
custom_colors = ['black', 'green']
cmap = ListedColormap(custom_colors)

# ==========================================
# 2. 初始状态设置
# ==========================================
# u 初始为 1.0 (充满底质)
u = xp.ones((N, N), dtype=xp.float64)
# u = xp.zeros((N, N))
# v 初始为 0.0 (无激活剂)
v = xp.zeros((N, N), dtype=xp.float64)

# 加入初始扰动 (在中心撒下一小块“种子”)
# 这就是打破对称性的初始“噪声”
r = 25
center = N // 2
# u[center-r:center+r, center-r:center+r] = 1
# v[center-r:center+r, center-r:center+r] = 0.2
# Randomly generate points across
# v[center-r:center+r, center-r:center+r] = 0.8
# v += xp.random.random((N, N)) * 0.2

num_seeds = 30  # 种子数量
for _ in range(num_seeds):
    r = 5 # 种子半径
    cx, cy = np.random.randint(r, N-r, 2)
    # 核心：v 上升，u 下降
    u[cx-r:cx+r, cy-r:cy+r] = 1
    v[cx-r:cx+r, cy-r:cy+r] = 0.3

# 加入全局微量随机噪声
# u += np.random.random((N, N)) * 0.4
# v += np.random.random((N, N)) * 0.1

# ==========================================
# 3. 核心算法 (拉普拉斯与迭代)
# ==========================================
def laplacian(Z):
    """
    计算离散拉普拉斯算子
    使用 roll 实现周期性边界条件 (环形拓扑)；GPU 上由 CuPy 执行
    """
    return (xp.roll(Z, 1, axis=0) + xp.roll(Z, -1, axis=0) +
            xp.roll(Z, 1, axis=1) + xp.roll(Z, -1, axis=1) - 4 * Z)

def update(frame):
    global u, v
    
    # 为了动画流畅，每一帧动画进行多次物理计算
    for _ in range(40):
        # 计算扩散项
        lu = laplacian(u)
        lv = laplacian(v)
        
        # 计算反应项 uv^2 (自催化)
        uv2 = u * v**2
        
        # Gray-Scott 方程更新
        # du/dt = Du*lap(u) - uv^2 + F(1-u)
        # dv/dt = Dv*lap(v) + uv^2 - (F+k)v
        u += (Du * lu - uv2 + F * (1.0 - u)) * dt
        v += (Dv * lv + uv2 - (F + k) * v) * dt

        # 数值稳定性限制
        u = xp.clip(u, 0, 1)
        v = xp.clip(v, 0, 1)

    # 更新图像数据（matplotlib 需要 CPU 数组，GPU 时拷贝回主机）
    im.set_array(xp.asnumpy(v) if _GPU else v)
    return [im]

# ==========================================
# 4. 动画展示
# ==========================================
fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(xp.asnumpy(v) if _GPU else v, cmap=cmap, interpolation='bilinear')
ax.set_title(f"Turing Pattern (F={F}, k={k})" + (" [GPU]" if _GPU else " [CPU]"))
ax.axis('off')

# 创建实时动画
ani = FuncAnimation(fig, update, frames=200, interval=1, blit=True)

plt.show()

print("模拟已启动。" + (" 使用 GPU (CuPy)。" if _GPU else " 使用 CPU (NumPy)。"))
print("你可以尝试调整代码中的 F 和 k 来观察模式的改变。")