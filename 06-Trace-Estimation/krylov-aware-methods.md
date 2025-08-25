---
title: Krylov Aware Methods
description: Advanced trace estimation methods that combine Krylov subspace techniques with variance reduction
keywords: [Krylov aware methods, Krylov subspace, variance reduction, trace estimation, subspace methods, convergence acceleration]
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

It's natural to combine Krylov subspace methods with [variance reduction techniques](./variance-reduction.ipynb) for trace estimation.
This can lead to improvements over [Stochastic Lanczos Quadrature](./stochastic-Lanczos-quadrature.md), which is based on the [Girard-Hutchinson estimator](./girard-hutchinson.md).
Krylov aware methods take this one step further, by making use of  interaction between Krylov subspace methods and randomized low-rank approximation techniques to more efficiently produce low-rank approximations to matrix functions {cite:p}`chen_hallman_23,persson_chen_musco_25`.

Let's consider a [Randomized-SVD](../05-Low-Rank-Approximation/randomized-svd.ipynb#alg-randomized-svd) type approach to obtaining a low-rank approximation to $f(\vec{A})$, where products with $f(\vec{A})$ are approximated via Krylov subspace methods.

:::{prf:algorithm} Randomized SVD with KSM
:label: alg-randomized-svd-ksm
**Input:** Matrix $\vec{A} \in \mathbb{R}^{n \times n}$, function $f$

1. Sample random Gaussian matrix $\vec{\Omega}$
1. Use KSM to compute approximation $\vec{Y}$ to $f(\vec{A})\vec{\Omega}$
1. Compute orthornomal basis $\vec{Q}$ for $\vec{Y}$
1. Use KSM to compute approximation $\vec{X}$ to $f(\vec{A}) \vec{Q}$ using KSM

**Output:** $\vec{Q}\vec{X}^\T$
:::


The first key observation is that $\vec{Y}$ is contained in some block Krylov subspace 
\begin{equation}
\mathcal{K}_s(\vec{A},\vec{\Omega}) =
\text{span}\{\vec{\Omega}, \vec{A}\vec{\Omega}, \vec{A}^2\vec{\Omega}, \ldots, \vec{A}^{s-1}\vec{\Omega}\},
\end{equation}
where $s$ is the number of steps taken by the KSM.

Let $\vec{Q}_{s}$ be an orthonormal basis for $\mathcal{K}_s(\vec{A},\vec{\Omega})$.
We can compute $\vec{Q}_{s}$ using the same number of matrix-vector products with $\vec{A}$ as were used to compute $\vec{Y}$.
However, $\range(\vec{Q})\subseteq \range(\vec{Q}_{s})$, so we may expect that $\vec{Q}_{s}\vec{Q}_{s}^\T f(\vec{A})$ is a better approximation to $f(\vec{A})$ than $\vec{Q}\vec{Q}^\T f(\vec{A})$.

However, since $\vec{Q}_{s}$ has many more columns than $\vec{Q}$, at first glance computing an approximation to $f(\vec{A})\vec{Q}_{s}$ seems to require many more products than computing an approximation to $f(\vec{A})\vec{Q}$.

The second key observation that because $\vec{Q}_{s}$ is a basis for a Krylov subspace, we can efficiently compute an approximation to $f(\vec{A}) \vec{Q}_{s}$.
In particular, we have the following:
:::{prf:proposition} Krylov subspaces of Krylov subspaces are Krylov subspaces
:label: prop-ksm-ksm
Suppose $\vec{Q}_{s}$ is a basis for the block Krylov subspace $\mathcal{K}_s(\vec{A},\vec{\Omega})$.
Then $\mathcal{K}_{r+1}(\vec{A},\vec{Q}_{s}) = \mathcal{K}_{s+r}(\vec{A},\vec{\Omega})$.
:::

:::{prf:proof}
:class: dropdown
:enumerated: false
\begin{equation*}
\begin{aligned}
    \mathcal{K}_{r+1}(\bm{A},\bm{Q}_s) &= \range\big( \big[ \bm{Q}_s \,\bm{A}\bm{Q}_s \, \cdots \, \bm{A}^r\bm{Q}_s \big]\big)\\
    &=  \range\big( \big[\bm{\Omega} \,\hspace{5pt}\bm{A}\bm{\Omega} \, \hspace{5pt}\cdots\hspace{5pt} \, \bm{A}^r\bm{\Omega}\\% First line
    &\hspace{2.2cm} \bm{A} \bm{\Omega} \,\hspace{5pt} \bm{A}^2\bm{\Omega} \, \cdots \, \bm{A}^{r+1} \bm{\Omega}\\
    & \hspace{3.5cm} \ddots\\
    & \hspace{3.5cm} \bm{A}^r \bm{\Omega} \,\hspace{5pt}\bm{A}^{r+1} \bm{\Omega} \,\hspace{5pt} \cdots \, \bm{A}^{s+r-1} \bm{\Omega} \big] \big) 
    \\&= \mathcal{K}_{s+r}(\bm{A},\bm{\Omega}). 
\end{aligned}
\end{equation*}
:::


This means that quantities such as $\vec{Q}_s^\T f(\vec{A}) \vec{Q}_s$ can be approximated from $\mathcal{K}_{s+r}(\vec{A},\vec{\Omega})$.
This requires just $nr$ additional matrix vector products with $\vec{A}$, rather than $n(q+1)$.

While this idea is simple, our algorithm can often perform much better than if matrix-vector products with $f(\vec{A})$ are treated as a black box. 
This is particularly true for functions like $f(x) = \sqrt{x}$, where we may require $q$ to be quite large to obtain a good approximation to $f(\vec{A}) \vec{\Omega}$, but even the basis obtained with $q=1$ (which is basically like sketching $\vec{A}$) works well. 

Similar ideas are explored in {cite:p}`persson_kressner_23,persson_meyer_musco_25` where it is shown that sketching $\vec{A}$ instead of $f(\vec{A})$ is a good idea for operator monotone functions.



