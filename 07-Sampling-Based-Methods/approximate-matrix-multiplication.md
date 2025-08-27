---
title: Approximate Matrix Multiplication
description: Sampling-based algorithms for fast approximate matrix multiplication using row and column sampling
keywords: [approximate matrix multiplication, row sampling, column sampling, importance sampling, communication-efficient algorithms, sparse matrices]
numbering:
  equation:
    enumerator: 7.%s
    continue: true
  proof:theorem:
    enumerator: 7.%s
    continue: true
  proof:algorithm:
    enumerator: 7.%s
    continue: true
  proof:definition:
    enumerator: 7.%s
    continue: true
  proof:proposition:
    enumerator: 7.%s
    continue: true
---


Approximate matrix-multiplication is the quintessential example of a sampling-based RandNLA algorithm {cite:p}`drineas_kannan_mahoney_06`.
Consider the matrix-matrix product
```{math}
:label: eqn-matmat
\vec{A}\vec{B}^\T = \sum_{i=1}^{n}
\vec{a}_i \vec{b}_i^\T
,\qquad
\vec{A} 
= \begin{bmatrix}
| & & | \\
\vec{a}_1 & \cdots & \vec{a}_n \\
| & & |
\end{bmatrix}
,\quad
\vec{B}:=
\begin{bmatrix}
| & & | \\
\vec{b}_1 & \cdots & \vec{b}_n \\
| & & |
\end{bmatrix}.
```

We can approximate {eq}`eqn-matmat` by sampling. 
In particular, consider a probability distribution $\mathcal{P} := (p_1, \ldots, p_n)$ on the indices $\{1, \ldots, n\}$ such that if $s\sim \mathcal{P}$ then $\PP[s=i] = p_i$.
Then clearly, 
```{math}
\EE\left[ \frac{1}{p_s}\vec{a}_s \vec{b}_s^\T \right]
= \vec{A}\vec{B}^\T.
```
This suggests a simple estimator.

:::{prf:definition}
Fix an integer $m\geq 1$. The *approximate matrix multiplication estimator* corresponding to the distribution $\mathcal{P}$ is 
\begin{equation*}
\Call{AMM}_m(\vec{A},\vec{B}) := 
\frac{1}{m} \sum_{i=1}^{m} \frac{1}{p_{s_i}} \vec{a}_{s_i} \vec{b}_{s_i}^\T,
\end{equation*}
where $\vec{s}_1,\ldots, \vec{s}_m$ are iid samples from $\mathcal{P}$.
:::

## Variance Bound

One can directly compute the variance of the approximate matrix multiplication estimator.

:::{prf:theorem}

For any $\vec{A}$ and $\vec{B}$, $\EE\left[\Call{AMM}_m(\vec{A},\vec{B}) \right] = \vec{A}\vec{B}^\T$ and
\begin{equation*}
\EE\left[ \| \vec{A}\vec{B} - \Call{AMM}_m(\vec{A},\vec{B}) \|_\F^2 \right]
= \frac{1}{m}\left( \sum_{i=1}^{n} p_i^{-1} \| \vec{a}_i \|^2 \| \vec{b}_i \|^2 - \|\vec{A}\vec{B}\|_\F^2\right).
\end{equation*}

:::

:::{prf:proof}
:class: dropdown
:enumerated: false

Clearly the estimator is unbiased, and by basic [properties of the expectation](../01-Background/review.md#properties-of-the-expectation), 
\begin{equation*}
\begin{aligned}
\EE[ \| \vec{A}\vec{B} - \Call{AMM}_m(\vec{A},\vec{B}) \|_\F^2] 
&= m^{-1} \EE[ \| \vec{A}\vec{B} - \Call{AMM}_1(\vec{A},\vec{B}) \|_\F^2] 
\\&= m^{-1} (\EE[ \Call{AMM}_1(\vec{A},\vec{B}) \|_\F^2] - \|\vec{A}\vec{B}\|_\F^2).
\end{aligned}
\end{equation*}
Now, by direct computation,
\begin{equation*}
\begin{aligned}
\EE[ \Call{AMM}_1(\vec{A},\vec{B}) \|_\F^2] 
&= \EE\left[ \left\| p_s^{-1}\vec{a}_s \vec{b}_s^\T \right\|_\F^2\right]
\\&= \sum_{i=1}^{n} p_i \left\| p_i^{-1}\vec{a}_i \vec{b}_i^\T \right\|_\F^2
\\&= \sum_{i=1}^{n} p_i^{-1} \| \vec{a}_i \|^2 \| \vec{b}_i \|^2.
\end{aligned}
\end{equation*}
:::

In particular, note that if $p_i \propto \|\vec{a}_i\|^2$ (or $p_i \propto \|\vec{b}_i\|^2$), then
```{math}
:label: eqn-amm-row-norms
\EE\left[ \| \vec{A}\vec{B} - \Call{AMM}_m(\vec{A},\vec{B}) \|_\F^2 \right]
= \frac{1}{m}\left( \|\vec{A}\|_\F^2\|\vec{B}\|_\F^2 - \|\vec{A}\vec{B}\|_\F^2\right).
```