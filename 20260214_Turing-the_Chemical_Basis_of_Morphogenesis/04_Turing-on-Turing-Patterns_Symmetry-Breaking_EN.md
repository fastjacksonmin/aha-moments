# Turing on Turing Patterns – Chapter 4: Symmetry Breaking Explained with Elementary Math

> Hickory dickory dock, the mouse climbed up the rod...
>
> The mouse went up, the rod went down...
>
> Hickory dickory dock.


## 1. A Dimensionality Reduction with Only Arithmetic

In Chapter 4, Turing still does not use Fourier analysis. Instead, he relies on elementary arithmetic to explain how symmetry breaking arises in biological systems. Although the math looks simple, it is absolutely worth sitting down with pen and paper to work through the derivation yourself and understand why these parameters were chosen.

Before beginning the derivation, however, Turing raises a paradox that should make every physicist slightly uncomfortable: why aren’t living organisms spherical?


## 2. The “Spherical Horse” and a Subtle Logical Error

Turing points out that an early embryo (the blastula) is nearly perfectly spherical and symmetric. According to classical determinism in physics, if the initial state and the governing laws are symmetric, then the system should remain symmetric forever. We would end up with a “spherical horse.”

This echoes the physicists’ self‑mocking joke about studying a “spherical chicken in vacuum.”

The hidden logical mistake lies in how we used to treat small random deviations in embryos: we assumed they could be ignored. Turing takes the opposite stance. These tiny deviations are not negligible — they are the ticket that allows the system to enter instability.

Noise provides the “push” that breaks symmetry, while physical law performs the “frequency selection” within chaos.


## 3. A Surprising Connection: The Oscillator Analogy

When I encountered Fourier analysis in Chapter 2, I was reminded of the Pierce oscillator I had recently been studying. In this chapter, Turing draws an analogy between electrical oscillators and biological morphogenesis. Discovering that my intuition aligned with Turing’s was deeply satisfying.

* **Noise as input**: Thermal noise is always present in electrical circuits.
* **Frequency selectivity**: Any perturbation matching the circuit’s natural frequency is captured and amplified.
* **Determinism vs randomness**: Circuit parameters (R, L, C, gain) determine waveform shape, while noise determines phase.

Although oscillator design in Turing’s era differed from modern implementations, the underlying principle remains the same.


## 4. The Biological RLC Network: Diffusion and Mass Action

If electrical oscillators rely on RLC networks and amplifiers to select and amplify specific frequencies, then in morphogenesis the analogous mechanisms are:

* **Mass Action (gain and nonlinearity)**: Determines who activates whom and who inhibits who*m.*
* **Diffusion (spatial coupling and filtering)**: Determines how signals communicate with neighbors.

Turing manually tunes the system into a delicate state:

* **X is the activator**: It accelerates itself and also promotes Y (positive feedback).
* **Y is the inhibitor**: It suppresses X and suppresses itself (negative feedback).
* **Ninefold diffusion ratio**: Y diffuses nine times faster than X

$$
D_X = 0.5, \quad D_Y = 4.5
$$

Reaction rates:

$$
\text{Rate of } X = 5X - 6Y + 1
$$

$$
\text{Rate of } Y = 6X - 7Y + 1
$$

This ninefold diffusion difference functions like a high‑Q frequency‑selective circuit in biology.


## 5. Arithmetic Derivation: How Diffusion “Betrays” Equilibrium

Turing constructs a model consisting of only two cells (Cell 1 and Cell 2). Suppose that due to random noise, the concentrations of X and Y in Cell 1 are just slightly higher than equilibrium.

* **Local celebration:** In Cell 1, X begins to amplify itself aggressively (the activator effect), while simultaneously producing a large amount of Y.

* **Brake failure:** Because Y diffuses extremely quickly, the Y just produced in Cell 1 does not remain long enough to suppress the local X. Instead, it rapidly diffuses into the neighboring cell.

A two-way catastrophe unfolds:

* **Cell 1:** Since the “brake” (Y) has escaped, X loses its constraint entirely, and its concentration rises exponentially.

* **Cell 2:** It is flooded by the Y diffusing in from next door. The X in Cell 2 is strongly suppressed.

This structure — **short-range positive feedback combined with long-range negative feedback** — transforms two originally symmetric cells into a “peak” and a “valley” through nothing more than a few additions and subtractions.

If you are interested, you can find the detailed step-by-step arithmetic in the [Appendix](#appendix--reconstructing-turings-arithmetic).

## 6. Turing’s “Defensive” Modeling: A Hypothetical Biochemical Laboratory

After presenting the mathematical result, Turing realized that biologists might question whether such equations were chemically realistic. To demonstrate that the logic was physically implementable, he forcefully *constructed* five explicit chemical reaction schemes. 

Through these five reactions, Turing showed how a set of simple chemical steps can synthesize a seemingly sophisticated dynamical system.

* **(i) Constant background production:** Through precursor substances in the environment (A and B), X and Y are continuously generated, providing a baseline concentration for the system (rate = 1).

* **(ii) Natural decay:** Y spontaneously degrades into an inert substance D (rate = $7Y$).

* **(iii) Conversion:** The activator X is converted into the inhibitor Y (rate = $6X$).

* **(iv) Autocatalysis (the core gain mechanism):** This is the most elegant step. Turing assumes that X catalyzes its own production. Through an unstable intermediate $U$ ($A + X \rightarrow 2X$), exponential growth of X is achieved (rate = $11X$).

* **(v) Catalytic consumption:** Using another catalyst C, Y proportionally consumes X (rate = $6Y$).

### Mathematical Confluence

If we sum these five processes, we obtain exactly the reaction equations introduced earlier:

* For X:

$$
1 (\text{i}) - 6X  (\text{iii}) + 11X (\text{iv}) - 6Y (\text{v}) = 5X - 6Y + 1
$$

* For Y:

$$
1 (\text{i}) + 6X (\text{iii}) - 7Y (\text{ii}) = 6X - 7Y + 1
$$

Turing was not merely playing with algebra. He was conducting what we would now call a **feasibility study**. Through this hypothetical biochemical laboratory, he demonstrated that even if nature does not literally use these exact equations, the *activator–inhibitor logic* can indeed be realized through ordinary chemical pathways.


## 7. The Mouse Climbing up the Rod: A Smooth Transition from Stability to Instability

At the end of this chapter, Turing demonstrates remarkable modeling intuition. He admits that the system we previously constructed breaks symmetry because its parameters were already placed inside an unstable region. But then he raises a deeper question: how could nature deliberately construct a system that is unstable from the very beginning?

To resolve this, he introduces a metaphor about gradual parameter evolution — **a mouse climbing up a rod**.

Imagine a rigid rod pivoted slightly above its center of mass.

* At first, the rod is stable. If you gently push it left or right, it swings but eventually returns to its lowest equilibrium position.

* Now imagine a small mouse climbing onto the rod and slowly moving upward. As long as the mouse remains below the center of mass, the system is still stable. Any small disturbance will eventually decay, and the rod will return to balance.

* But the moment the mouse climbs past the center of mass, something profound changes. The rod is still technically in "equilibrium," yet it has become exquisitely unstable. A slight twitch of the mouse’s whiskers is enough to tip the rod irreversibly to one side.

The equilibrium did not disappear — its *stability* changed sign.

How does this metaphor connect to the reaction equations? Turing introduces a parameter (I), representing the height of the mouse — that is, the strength of the underlying developmental parameters.

Turing introduces a parameter (I) representing developmental progression:

$$
\text{Rate of } X = (3+I)X - 6Y + I -1
$$

$$
\text{Rate of } Y = 6X - (9+I)Y - I + 1
$$

* If ($I < 0$): stable and symmetric.
* As ($I \to 0$): system approaches criticality.
* If ($I > 0$): instability emerges.

At ($I = 2$), we recover the previously discussed system.

Turing humorously writes:

> “The system which was originally discussed was the case (I=2), and might be supposed to correspond to the mouse somehow reaching the top of the pendulum without disaster, perhaps by falling vertically on to it.”

The increase of (I) acts as a developmental clock.

## Possible Misprint in the Y Production Rate?

If you take one more step and substitute (I = 2) into the rate equation, you will notice a serious problem: although the production rate of X matches perfectly, the production rate of Y does not.

Starting from the expression as printed:

$$
ext{Rate of } Y = 6X - (9+I)Y - I + 1
$$

Substituting (I = 2):

$$
6X - (9+2)Y - 2 + 1 = 6X - 11Y - 1
$$

This clearly does not agree with the earlier expression we discussed for the production rate of Y.

For this reason, I suspect there may have been a typographical error in the printing process. The intended expression may instead have been:

$$
6X - (9 - I)Y + I - 1
$$

What do you think?

## Reflections

Through what looks like nothing more than elementary school arithmetic, Turing teaches us something profound: morphogenesis is not the execution of a pre-written blueprint, but a **constrained instability**.

Noise determines the *phase* — which cell begins to oscillate first. But physical law determines the *waveform* — what kind of pattern ultimately emerges.

This perspective, established in 1952, still sends a quiet shiver down the spine of any engineer who attempts to understand complexity. It suggests that order is not imposed from above; it is selected from within instability.
