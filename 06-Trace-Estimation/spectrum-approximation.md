---
title: Spectrum approximation
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

:::{prf:definition}

The *spectral density* of $\vec{A}$ is the probability density 
\begin{equation*}
\varphi(x;\vec{A}) := \frac{1}{n} \sum_{i=1}^{n} \delta(x - \lambda_i),
\end{equation*}
where $\delta(x)$ is the Dirac delta at zero.

:::

We are interested in a coarse approximation to the spectral density of $\vec{A}$; e.g. in Wasserstein distance.
:::{prf:definition}
Let $\varphi_1(x)$ and $\varphi_2(x)$ be two densities with cumultive distribution functions $\Phi_1(z) := \int_{-\infty}^{z} \varphi_1(x) \d{x}$ and $\Phi_2(z) := \int_{-\infty}^{z} \varphi_2(x) \d{x}$ respectively. 
Then the *Wasserstein distance* between $\varphi_1$ and $\varphi_2$ is 
\begin{equation*}
\operatorname{W}(\varphi_1,\varphi_2) := \int_{-\infty}^{\infty} | \Phi_1(x) - \Phi_2(x) | \d{x}.
\end{equation*}
:::


## Relation to spectral sums

Spectrum approximation is closely related to the task of approximating [spectral sums](./matrix-functions.md).
Observe that 
```{math}
\tr(f(\vec{A})) = n\int_{-\infty}^{\infty} f(x) \varphi(x;\vec{A}) \d{x},
```
Likewise,
```{math}
\Phi(z) := \int_{-\infty}^{z} \varphi(x;\vec{A}) \d{x} = \tr(f_z(\vec{A})),\quad f_z(x) = \begin{cases}
n^{-1} & \text{if } x \leq z,\\
0 & \text{otherwise.}
\end{cases}
```
Hence approximating the spectral density and approximating spectral sums are equivalent; i.e. being able to approximate spectral sums gives us a way to approximate spectral densities and vise-versa.

