# Appendix – How Did Turing Actually Do This Arithmetic?

If Chapter 4 reads like a tongue‑twister, it is because Turing is verbally describing a stepwise calculation of a coupled system of differential equations.

Let us unfold the chemical reactions and diffusion terms of these two cells (Cell 1 and Cell 2) the way an engineer would audit a balance sheet.

---

## 1. System Configuration

For this “two‑cell circuit,” Turing pre‑configures two layers of logic.

### A. Reaction Rate Equations: The Contest Between Activation and Inhibition

This is the soul of the system. By simply inspecting the signs of the coefficients, we can immediately read the “personality” of X and Y.

Rate of X:

$$
f(X, Y) = 5X - 6Y + 1
$$

Rate of Y:

$$
g(X, Y) = 6X - 7Y + 1
$$

* **X: the ambitious activator**

  * Look at the coefficients of X ((+5) and (+6)).

  * **Self‑catalysis:** In the first equation, X positively feeds back on itself ((+5X)). The more X there is, the faster it grows.

  * **Faction expansion:** In the second equation, X also promotes the production of Y ((+6X)).

  * **Conclusion:** X is an activator. It constantly presses the accelerator, attempting to increase everything — including its own adversary.

* **Y: the cold inhibitor**

  * Look at the coefficients of Y ((-6) and (-7)).

  * **External suppression:** In the first equation, Y strongly suppresses X ((-6Y)). The more Y there is, the faster X is consumed.

  * **Self‑restraint:** In the second equation, Y even suppresses itself ((-7Y)).

  * **Conclusion:** Y is an inhibitor. Its role is to press the brake, maintain order, and prevent X from running out of control.

### B. Diffusion Constants: The Contest Between Fast and Slow

$$
D_X = 0.5
$$

Slow diffusion: the activator X is relatively “home‑bound.” Once produced, it tends to remain local.

$$
D_Y = 4.5
$$

Fast diffusion: the inhibitor Y runs quickly — nine times faster than X — and readily “interferes” with its neighbor.

---

## 2. Equilibrium

First, verify the steady state. When both cells maintain concentrations

$$
X = 1, \quad Y = 1
$$

the system is in silent equilibrium.

Chemical balance:

$$
5(1) - 6(1) + 1 = 0
$$

$$
6(1) - 7(1) + 1 = 0
$$

Diffusion balance:

Since the concentrations are equal ((\Delta X = 0, \Delta Y = 0)), no substance crosses the cell boundary.

---

## 3. The Small‑Signal Perturbation

Now noise breaks the calm:

Cell 1:

$$
X_1 = 1.06, \quad Y_1 = 1.02
$$

Cell 2:

$$
X_2 = 0.94, \quad Y_2 = 0.98
$$

---

## 4. Time to Do the Accounting: Why Does Symmetry Break?

Take Cell 1 as an example and examine the “financial statement” of its X concentration.

### A. Reaction Flux

$$
\Delta X_{react} = 5(1.06) - 6(1.02) + 1 = +0.18
$$

### B. Diffusion Flux

$$
\Delta X_{diff} = 0.5 \cdot (0.94 - 1.06) = -0.06
$$

### C. Net Change

$$
\text{Net } \Delta X_1 = +0.18 - 0.06 = +0.12
$$

**Conclusion:** When the X concentration in Cell 1 exceeds equilibrium by 0.06, in the next step it increases by 0.12 — exactly twice its deviation.

This is one of the most satisfying hand‑calculations in the entire paper. Turing carefully selected these numbers to engineer a perfect **doubling effect**.

### Aha Moment

The growth rate of the difference (0.12) is exactly twice the difference itself (0.06).

Meanwhile, in Cell 2, the opposite occurs. When X is below equilibrium by 0.06, in the next step it decreases by 0.12.

In this arithmetic model, the difference between the two cells grows geometrically — doubling at each time step.

This mathematical elegance not only makes the paper readable, but also provides an intuitive definition of instability: **difference itself becomes the fuel for further growth.**

---

## 5. A Striking Conclusion

Although diffusion — the smoothing force — is working hard, the strong activator gain of X and the rapid escape of the inhibitor Y create spatial asymmetry.

In Cell 1:

The newly produced inhibitor Y rapidly escapes. The activator X therefore loses its restraint completely.

In Cell 2:

It is flooded by the inhibitor arriving from its neighbor. The X in Cell 2 is further suppressed.

---

## 6. If Turing Had Met Laozi

This reminds me of a passage from the *Dao De Jing*:

> The Way of Heaven reduces excess and supplements deficiency.
> The way of man is different: it reduces the deficient to serve the excessive.

If Turing had met Laozi, perhaps he would have replied:

“Master, whether one reduces the excessive or serves the excessive, both belong to the Way of Heaven. But only the latter allows life to break the symmetry of stillness and step onto the path of existence.”
