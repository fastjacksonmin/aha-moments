import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ==========================================
# 1. 模拟参数设置 (调节旋钮)
# ==========================================
# 网格尺寸
N = 200              

# 扩散系数 (Diffusivity)
# Dv 必须显著小于 Du 才能产生稳定的图灵模式
Du, Dv = 0.16, 0.08  

# 反应参数 (F 和 k 是大自然的“旋钮”)
# 尝试以下组合:
# 斑点 (Spots): F=0.030, k=0.062
# 斑马纹 (Stripes): F=0.042, k=0.060
# 迷宫 (Maze): F=0.035, k=0.060
# 细胞分裂 (Mitosis): F=0.036, k=0.064
F = 0.035            
k = 0.062

dt = 1.0             # 时间步长

# ==========================================
# 2. 初始状态设置
# ==========================================
# u 初始为 1.0 (充满底质)
u = np.ones((N, N))
# v 初始为 0.0 (无激活剂)
v = np.zeros((N, N))

# 加入初始扰动 (在中心撒下一小块“种子”)
# 这就是打破对称性的初始“噪声”
r = 10
center = N // 2
u[center-r:center+r, center-r:center+r] = 0.5
v[center-r:center+r, center-r:center+r] = 0.25

# 加入全局微量随机噪声
u += np.random.random((N, N)) * 0.02
v += np.random.random((N, N)) * 0.02

# ==========================================
# 3. 核心算法 (拉普拉斯与迭代)
# ==========================================
def laplacian(Z):
    """
    计算离散拉普拉斯算子
    使用 np.roll 实现周期性边界条件 (环形拓扑)
    """
    return (np.roll(Z, 1, axis=0) + np.roll(Z, -1, axis=0) +
            np.roll(Z, 1, axis=1) + np.roll(Z, -1, axis=1) - 4 * Z)

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
        u = np.clip(u, 0, 1)
        v = np.clip(v, 0, 1)

    # 更新图像数据
    im.set_array(v)
    return [im]

# ==========================================
# 4. 动画展示
# ==========================================
fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(v, cmap='magma', interpolation='bilinear')
ax.set_title(f"Turing Pattern (F={F}, k={k})")
ax.axis('off')

# 创建实时动画
ani = FuncAnimation(fig, update, frames=200, interval=1, blit=True)

plt.show()

print("模拟已启动。你可以尝试调整代码中的 F 和 k 来观察模式的改变。")