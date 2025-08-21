---
title: Girard-Hutchinson Estimator
description: Fundamental unbiased estimator for matrix traces using random vectors and variance analysis
keywords: [Girard-Hutchinson estimator, Hutchinson trace estimator, unbiased estimator, variance bounds, Gaussian vectors, Rademacher vectors]
numbering:
  equation:
    enumerator: 6.%s
    continue: true
  proof:theorem:
    enumerator: 6.%s
    continue: true
  proof:algorithm:
    enumerator: 6.%s
    continue: true
  proof:definition:
    enumerator: 6.%s
    continue: true
  proof:proposition:
    enumerator: 6.%s
    continue: true
---

## Girard-Hutchinson Estimator

Let $\vec{x}$ be a random vector satisfying $\mathbb{E}[\vec{x}] = \vec{0}$ and $\mathbb{E}[\vec{x}\vec{x}^\T] = \vec{I}$.
Then, a direct computations reveals that $\vec{x}^\T\vec{A}\vec{x}$ is an unbiased estimator of the trace of $\vec{A}$. 
In particular, by the cylic property of the trace and linearity of expectation,
\begin{equation}
\EE[ \vec{x}^\T \vec{A}\vec{x}] 
= \EE[ \tr(\vec{x}^\T \vec{A}\vec{x}) ] 
= \EE[ \tr(\vec{A}\vec{x}\vec{x}^\T ) ] 
= \tr(\vec{A}\EE[ \vec{x}\vec{x}^\T ] )
= \text{tr}(\vec{A}).
\end{equation}
This suggests a simple randomized estimator.
:::{prf:definition} Girard-Hutchinson Estimator
:label: def:girard_hutchinson_estimator
Fix an integer $m \geq 1$. The *Girard-Hutchinson trace estimator* is
\begin{equation*}
\widehat{\tr}_m(\vec{A}) := \frac{1}{m}\sum_{i=1}^{m} \vec{x}_i^\T \vec{A} \vec{x}_i,
\end{equation*}
where $\vec{x}_i$ are iid copies of some vector $\vec{x}$ satisfying $\mathbb{E}[\vec{x}] = \vec{0}$ and $\mathbb{E}[\vec{x}\vec{x}^\T] = \vec{I}$.
:::
```{aside} History
This estimator is often referred to as *Hutchinson's trace estimator*, especially when $\vec{x}$ is a random Rademacher vector.
However, {cite:p}`hutchinson_89` itself cites {cite:p}`girard_87` which addresses the same task by using samples of $\vec{x}$ drawn uniformly from the unit hypersphere.
See {cite:p}`chen_22` for more discussion.
```

## Variance Bounds

We can easily characterize the expectation and variance of the Girard-Hutchinson estimator when $\vec{x}$ is a Gaussian vector.
:::{prf:theorem}
Suppose $\vec{A}$ is symmatric and $\vec{x}_i$ are iid Gaussian vectors. 
Then
\begin{equation*}
\EE[ \widehat{\tr}_m(\vec{A}) ] = \tr(\vec{A}),
\qquad
\VV[ \widehat{\tr}_m(\vec{A}) ] = \frac{2\|\vec{A}\|_\F^2}{m}.
\end{equation*}
:::


:::{admonition} Proof
:class: dropdown
A standard computation reveals that 
\begin{equation*}
\EE[ \widehat{\tr}_m(\vec{A}) ] = \tr(\vec{A}),
\qquad
\VV[ \widehat{\tr}_m(\vec{A}) ] = \frac{1}{m} \VV[\vec{x}^\T\vec{A}\vec{x}].
\end{equation*}

Since $\vec{A}$ is symmetric, it has an eigendecomposition $\vec{A} = \vec{U}\vec{\Lambda}\vec{U}^\T$, where $\vec{U}\in\R^{n\times n}$ is an orthogonal matrix and $\vec{\Lambda} = \text{diag}(\lambda_1,\ldots,\lambda_n)$ is a diagonal matrix.
By the [Gaussian orthogonal invariance property](../02-Sketching/Gaussian-sketch.ipynb#prop:gaussian-orthogonal-invariance), $\vec{z} = \vec{U}\vec{x}$ is also a Gaussian vector.
Observe that 
\begin{equation*}
\vec{x}^\T\vec{A}\vec{x} = \vec{z}^\T\vec{\Lambda}\vec{z} = \sum_{i=1}^{n} \lambda_i z_i^2.
\end{equation*}
Since $z_i^2$ are independent $\chi^2_1$ random variables, we have,
\begin{equation*}
\VV[\vec{x}^\T\vec{A}\vec{x}] = \sum_{i=1}^{n} \lambda_i^2 \VV[z_i^2] = \sum_{i=1}^{n} \lambda_i^2 \cdot 2 = 2\|\vec{A}\|_\F^2.
\end{equation*}
:::
If $\vec{A}$ is not symmetric, we can use the fact that $\widehat{\tr}_m(\vec{A})=\widehat{\tr}_m((\vec{A} + \vec{A}^\T)/2)$.

### Other Distributions

Besides Gaussian, two commonly used distributions are:
- **Rademacher:** Each component of $\vec{x}$ is iid $\{-1,1\}$ with equal probability. 
- **Random unit vector (real):** Each component of $\vec{x}$ is iid $\mathcal{N}(0,1)$, and then $\vec{x}$ is normalized to have norm $\sqrt{n}$.

When $\vec{A}$ is symmetric, the variance of the estimator can be computed explicitly:
| Distribution of $\vec{x}$ | Variance |
|-------|-----|
| Gaussian     | $\frac{1}{m} \cdot 2 \Vert\vec{A}\Vert_\F^2$ |
|  Rademacher  | $\frac{1}{m} \cdot 2 (\Vert\vec{A}\Vert_\F^2 - \sum_i A_{ii}^2)$ |
| Uniform (real)     | $\frac{1}{m} \cdot \frac{2n}{n+2} \left( \Vert \vec{A} \Vert_\F^2 - \frac{1}{n}\tr(\vec{A})^2 \right)$ |

Deriving the variance for Rademacher vectors is a straightforward (but tedious) exercise in basic probability. 
The variance for the uniform distribution can also be derived from elementary techniques, but requires some care to handle the normalization. 
Readers can refer to Ethan's [blog post](https://www.ethanepperly.com/index.php/2023/01/26/stochastic-trace-estimation/) for a derivation of the variances listed above, as well as some additional discussion on interesting optimality properties of certain distributions.


```{bibliography}
:filter: docname in docnames
```