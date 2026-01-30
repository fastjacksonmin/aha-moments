# Geometric Intuition of Linear Regression: From Algebra to Geometry

> "Through geometry we understand, but through algebra we transcend."

Linear regression is often taught as a set of laborious algebraic calculations to minimize error and find parameters $k$ and $b$ for the line $y = kx + b$. However, there is a much more intuitive way to understand it by switching from complex equations to a simplified geometric interpretation.

Here is the step-by-step breakdown of this geometric insight:

## 1. A Radical Change of View

Instead of the traditional method of plotting data points on a 2D $X$-$Y$ plane, let's flip our perspective. Imagine treating each measurement $(y_1, y_2, \dots, y_n)$ as its own axis.

**The Challenge:** Visualizing an $N$-dimensional space for $N$ data points is impossible for the human brain.

**The Simplification:** Let's stick to a simple case with just 3 measurements. Now, we can fit our entire interpretation into a relatable 3D space.

## 2. The "Observation Point"

In this $y_1$-$y_2$-$y_3$ space, your entire dataset—no matter how messy it looked on a scatter plot—collapses into a single point: $(y_1, y_2, y_3)$.

We call this the **Observation Point** (or **Observation Vector**). It hangs in the 3D space, representing the reality we measured.

## 3. The "Fitting Plane"

To fit this data with the model $y = kx + b$, we use our independent variables $(x_1, x_2, x_3)$ and a constant term.

As we vary the parameters $k$ and $b$ freely, the possible predictions sweep out a 2D plane embedded within this 3D space.

This plane represents all possible models we could create. If a point lies on this plane, it can be perfectly explained by $y = kx + b$.

## 4. Least Squares = Shortest Distance

Usually, our Observation Point does not lie on this perfect plane (because reality has noise).

The error of any fit is simply the Euclidean distance between the Observation Point and a point on the plane.

**Geometric Insight:** To minimize this error, we don't need calculus. We just need to find the point on the plane closest to our Observation Point.

Geometry tells us this occurs exactly where we drop a perpendicular line from the Observation Point to the plane. This landing spot is the **Least Squares solution**!

## 5. Degrees of Freedom: The Dimensionality that Error Vector Lives

As we add more data points, the total error (distance) naturally grows. To compare goodness-of-fit fairly across different dataset sizes, we need a "normalization factor."

**The Logic:** We shouldn't average the error over all $N$ dimensions, because we "used up" some dimensions to build our model.

**The Calculation:** We determine the dimension of the space where the "residual vector" (the error line) lives. In our 3D case, the model plane takes up 2 dimensions, leaving $3 - 2 = 1$ dimension for the error.

**The Result:** This remaining dimension $(N - k)$ is the **Degree of Freedom**. It represents the freedom of the noise to move orthogonally to the model. This is why we divide by $N-2$ (or $N-k$) instead of $N$ to get an unbiased estimate of variance:

$$\text{Unbiased Variance} = \frac{\text{Sum of Squared Residuals}}{N - k}$$

where $k$ is the number of parameters in the model.

## 6. Bonus Stage: The Simplest Regression

Some might think $y = kx + b$ is the simplest linear regression, but there is one simpler: $y = b$ (fitting a horizontal line).

The result of this fit is simply the group mean:

$$\bar{y} = \frac{1}{N} \sum_{i=1}^{N} y_i$$

When calculating the standard error (variance) of the mean, you divide by $N-1$:

$$s^2 = \frac{1}{N-1} \sum_{i=1}^{N} (y_i - \bar{y})^2$$

**Why?** Because you have 1 fitting parameter $(b)$, which consumes 1 dimension of the space. The error vector is left with $N-1$ degrees of freedom.

## 7. Transcend: Extend to N-dimensional world for N measurements

As the subtitle says, we understand through geometry, but we transcend through algebra. In real world, we have hundreds to millions of datapoints to fit. In that case, our brain is beyond the touch of visualizing it fully, and we have to rely on the math. However, this simple 3-D picture can also serve as the understanding point. 

**Credits:** This idea comes from *"Vector: A Surprising Story of Space, Time, and Mathematical Transformation"* by Robyn Arianrhod.

## The Demo

Open [`geometric-interpretation-of-linear-regression.html`](geometric-interpretation-of-linear-regression.html) in a browser. It shows a small example ($n=3$) in 3D: the observation $\mathbf{Y}$, the least-squares prediction $\hat{\mathbf{y}}$ on the column space, and the residual vector from $\hat{\mathbf{y}}$ to $\mathbf{Y}$.
