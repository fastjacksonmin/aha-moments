"""
Gray-Scott Turing pattern batch exploration.

Parametrized initial conditions and evolution for running long simulations
and comparing final patterns (no animation). Reference: turing-pattern.py
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from typing import Sequence

# ---------------------------------------------------------------------------
# 1. Initial conditions (parametrized)
# ---------------------------------------------------------------------------

def initial_condition(
    N: int,
    seed_centers: Sequence[tuple[int, int, int]] | tuple[int, int, int],
    v_seed: float = 0.25,
    u_seed: float = 1.0,
    noise_u: float = 0.04,
    noise_v: float = 0.02,
    random_seed: int | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Build u, v initial fields for Gray-Scott.

    seed_centers: (cx, cy, radius) or list of (cx, cy, radius). Each defines
                  a square patch where u=u_seed, v=v_seed.
    v_seed, u_seed: values inside the seed patch(es).
    noise_u, noise_v: amplitude of uniform [0,1] noise added globally.
    random_seed: for reproducibility.
    """
    if random_seed is not None:
        np.random.seed(random_seed)

    u = np.ones((N, N), dtype=np.float64)
    v = np.zeros((N, N), dtype=np.float64)

    # Normalize to single list of (cx, cy, r)
    if isinstance(seed_centers, (list, tuple)) and len(seed_centers) == 3:
        try:
            _ = seed_centers[0] + 0
        except TypeError:
            seed_centers = [seed_centers]
    else:
        seed_centers = list(seed_centers)

    for (cx, cy, r) in seed_centers:
        r0, r1 = max(0, cy - r), min(N, cy + r)
        c0, c1 = max(0, cx - r), min(N, cx + r)
        u[r0:r1, c0:c1] = u_seed
        v[r0:r1, c0:c1] = v_seed

    u += np.random.random((N, N)).astype(np.float64) * noise_u
    v += np.random.random((N, N)).astype(np.float64) * noise_v

    return u, v


# ---------------------------------------------------------------------------
# 2. Evolution (parametrized)
# ---------------------------------------------------------------------------

def laplacian(Z: np.ndarray) -> np.ndarray:
    """Discrete Laplacian with periodic boundary conditions."""
    return (
        np.roll(Z, 1, axis=0) + np.roll(Z, -1, axis=0)
        + np.roll(Z, 1, axis=1) + np.roll(Z, -1, axis=1)
        - 4 * Z
    )


def step(
    u: np.ndarray,
    v: np.ndarray,
    Du: float,
    Dv: float,
    F: float,
    k: float,
    dt: float,
) -> tuple[np.ndarray, np.ndarray]:
    """One Gray-Scott time step. Returns (u_next, v_next)."""
    lu = laplacian(u)
    lv = laplacian(v)
    uv2 = u * (v ** 2)
    u_next = u + (Du * lu - uv2 + F * (1.0 - u)) * dt
    v_next = v + (Dv * lv + uv2 - (F + k) * v) * dt
    u_next = np.clip(u_next, 0.0, 1.0)
    v_next = np.clip(v_next, 0.0, 1.0)
    return u_next, v_next


def evolve(
    u0: np.ndarray,
    v0: np.ndarray,
    Du: float,
    Dv: float,
    F: float,
    k: float,
    dt: float,
    n_steps: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Run Gray-Scott for n_steps. Returns (u_final, v_final)."""
    u, v = u0.copy(), v0.copy()
    for _ in range(n_steps):
        u, v = step(u, v, Du, Dv, F, k, dt)
    return u, v


# ---------------------------------------------------------------------------
# 3. Batch run: one or several (F, k), show final state(s)
# ---------------------------------------------------------------------------

# Defaults matching turing-pattern.py
N = 150
Du, Dv = 0.16, 0.08
dt = 1.0
n_steps = 10_000

# (F, k) presets from original comments
PRESETS = {
    "spots": (0.030, 0.062),
    "stripes": (0.042, 0.060),
    "maze": (0.035, 0.060),
    "mitosis": (0.036, 0.064),
}

custom_colors = ["#D7AC65", "#211309"]
cmap = ListedColormap(custom_colors)


def run_one(
    F: float,
    k: float,
    N: int = N,
    seed_centers: tuple[int, int, int] | None = None,
    random_seed: int | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Single run: build IC, evolve, return (u_final, v_final)."""

    if seed_centers is None:
        center = N // 2
        seed_centers = [(center, center, 10)]
    u0, v0 = initial_condition(
        N, seed_centers, random_seed=random_seed
    )
    return evolve(u0, v0, Du, Dv, F, k, dt, n_steps)


def example_one_and_grid_plot() -> None:
    # Example: run one preset and show final pattern
    F, k = PRESETS["spots"]
    _, v_final = run_one(F, k, random_seed=42)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(v_final, cmap=cmap, interpolation="bilinear")
    ax.set_title(f"Turing pattern (F={F}, k={k}), {n_steps} steps")
    ax.axis("off")
    plt.tight_layout()
    plt.savefig("turing-pattern-batch-one.png", dpi=120)
    plt.show()

    # Example: grid of four presets
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    for ax, (name, (F, k)) in zip(axes.flat, PRESETS.items(), strict=True):
        _, v_final = run_one(F, k, random_seed=42)
        ax.imshow(v_final, cmap=cmap, interpolation="bilinear")
        ax.set_title(f"{name} (F={F}, k={k})")
        ax.axis("off")
    plt.tight_layout()
    plt.savefig("turing-pattern-batch-grid.png", dpi=120)
    plt.show()

def main() -> None:
    # Example of randomly generate F and k based on PRESETS plus some random noise with 100 iterations
    for i in range(100):
        F_base, k_base = PRESETS[np.random.choice(list(PRESETS.keys()))]
        F = (1 + np.random.uniform(-0.5, 0.5)) * F_base
        k = (1 + np.random.uniform(-0.5, 0.5)) * k_base
        print(f"F: {F}, k: {k}")
        _, v_final = run_one(F, k, random_seed=None)
        plt.imshow(v_final, cmap=cmap, interpolation="bilinear")
        plt.title(f"Turing pattern (F={F:.3f}, k={k:.3f}), {n_steps} steps")
        plt.axis("off")
        plt.tight_layout()
        plt.savefig(f"20260131_Turing-pattern/results/turing-pattern-batch-random-{i}-F{F:.3f}-k{k:.3f}.png", dpi=120)
        # plt.show()


if __name__ == "__main__":
    main()
