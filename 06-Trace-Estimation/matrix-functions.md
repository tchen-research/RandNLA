---
title: Matrix function trace approximation
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
\begin{equation}
f(\vec{A}) := \sum_{i=1}^{n} f(\lambda_i) \vec{u}_i \vec{u}_i^\T.
\end{equation}

:::{prf:definition}

The  *spectral sum* of $\vec{A}$ and $f$ is defined as
\begin{equation*}
\tr(f(\vec{A})) = \sum_{i=1}^{n} f(\lambda_i).
\end{equation*}
:::

A natural approach is to combine the implicit trace estimation algorithms discussed earlier in this chapter with black-box methods for approximating $\vec{x}\mapsto \vec{x}^\T f(\vec{A})\vec{x}$ or $\vec{x}\mapsto f(\vec{A})\vec{x}$.

## Lanczos for matrix-functions

[Recall](../01-Background/review-NLA/#Krylov-subspace-methods), the Lanczos algorithm produces an orthonormal basis $\vec{Q}\in\R^{n\times k}$ for the Krylov subspace $\mathcal{K}_k(\vec{A}, \vec{x})$ and a symmetric tridiagonal matrix $\vec{T}\in\R^{k\times k}$ such that $\vec{T} = \vec{Q}^\T\vec{A}\vec{Q}$.

The output of the Lanczos method can then be used to approximate $f(\vec{A})\vec{x}$ and $\vec{x}^\T f(\vec{A})\vec{x}$.
This requires $k-1$ matrix-vector products with $\vec{A}$.

:::{prf:definition} Lanczos Method for matrix functions
:label: def:lanczos-method
The Lanczos approximations to $f(\vec{A})\vec{x}$ and $\vec{x}^\T f(\vec{A})\vec{x}$ are respectively given by
\begin{equation*}\begin{aligned}
\Call{Lan-FA}_k(f;\vec{A},\vec{x})&:= \|\vec{x}\|\vec{Q} f(\vec{T})\vec{e}_1 \\
\Call{Lan-QF}_k(f;\vec{A},\vec{x})&:=  \|\vec{x}\|^2\vec{e}_1^\T f(\vec{T})\vec{e}_1.
\end{aligned}\end{equation*}
:::

It is well-known that the accuracy of these approximations is related to how well $f(x)$ can be approximation by polynomials on the interval $[\lambda_n,\lambda_1]$.

:::{prf:theorem} 
:label: thm:lanczos_FA_polynomial
\begin{equation*}
\begin{aligned}
\| f(\vec{A})\vec{x} - \Call{Lan-FA}_k(f;\vec{A},\vec{x}) \| &\leq 2 \|\vec{x}\| \min_{\deg(p)<k} \left(\max_{x\in[\lambda_n,\lambda_1]} | f(x) - p(x) |\right) \\
| \vec{x}^\T f(\vec{A})\vec{x} - \Call{Lan-QF}_k(f;\vec{A},\vec{x}) | &\leq 2 \|\vec{x}\|^2 \min_{\deg(p)<2k-1} \left(\max_{x\in[\lambda_n,\lambda_1]} | f(x) - p(x) |\right).
\end{aligned}
\end{equation*}
:::

In particular, note that when $f(x)$ is a low-degree polynomial, the approximations are exact.

