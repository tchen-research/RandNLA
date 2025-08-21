---
title: Matrix function trace approximation and spectral densities
description: Computing traces of matrix functions and approximating spectral densities using randomized methods
keywords: [matrix functions, spectral sums, spectral density, eigenvalues, trace approximation, Dirac delta, probability measures]
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

Let $\vec{A}\in\R^{n\times n}$ be a symmetric matrix with eigendecomposition $\vec{A} = \sum_{i=1}^{n} \lambda_i \vec{u}_i \vec{u}_i^\T$, where $\lambda_i$ are the eigenvalues and $\vec{u}_i$ are the orthonormal eigenvectors of $\vec{A}$.
Recall the matrix function 
\begin{equation*}
f(\vec{A}) := \sum_{i=1}^{n} f(\lambda_i) \vec{u}_i \vec{u}_i^\T.
\end{equation*}

:::{prf:definition}

The  *spectral sum* of $\vec{A}$ and $f$ is defined as
\begin{equation*}
\tr(f(\vec{A})) = \sum_{i=1}^{n} f(\lambda_i).
\end{equation*}
:::

A natural approach is to combine the implicit trace estimation algorithms discussed earlier in this chapter with black-box methods for approximating $\vec{x}\mapsto \vec{x}^\T f(\vec{A})\vec{x}$ or $\vec{x}\mapsto f(\vec{A})\vec{x}$.



The task of matrix-function trace approximation is closely related to the task of estimating the spectrum of $\vec{A}$.

:::{prf:definition}

The *spectral density* of $\vec{A}$ is the probability measure 
\begin{equation*}
\varphi(x) := \frac{1}{n} \sum_{i=1}^{n} \delta(x - \lambda_i),
\end{equation*}
where $\delta(x)$ is the Dirac delta at zero$.

:::

We are interested approximating the spectral density of $\vec{A}$, as well a 

Observe that 
```{math}
\tr(f(\vec{A})) = n\int_{-\infty}^{\infty} f(x) \varphi(x) \d{x},
```
Likewise,
```{math}
\Phi(\alpha) := n\int_{-\infty}^{\alpha} \varphi(x) \d{x} = \tr(f_\alpha(\vec{A})),\quad f_\alpha(x) = \begin{cases}
1 & \text{if } x \leq \alpha,\\
0 & \text{otherwise.}
\end{cases}
```
Hence approximating the spectral density and approximating spectral sums are equivalent.

