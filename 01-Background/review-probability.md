---
title: Probability
description: Fundamental concepts in numerical linear algebra including factorizations, conditioning, stability, and the Lanczos method for matrix functions
keywords: [QR factorization, conditioning, stability, Lanczos method, matrix functions, Krylov subspace, numerical linear algebra]
numbering:
  equation:
    enumerator: 1.%s
    continue: true
  proof:theorem:
    enumerator: 1.%s
    continue: true
  proof:algorithm:
    enumerator: 1.%s
    continue: true
  proof:definition:
    enumerator: 1.%s
    continue: true
  proof:proposition:
    enumerator: 1.%s
    continue: true
---


## Properties of probability

:::{prf:theorem} Markov's Inequality
Let $X$ be a non-negative random variable. 
Then
\begin{equation*}
\PP[X\geq t] \leq \frac{\EE[X]}{t}.
\end{equation*}
:::

:::{prf:theorem} Chebyshev's Inequality
Let $X$ be a random variable. 
Then
\begin{equation*}
\PP[|X - \EE[X]| \geq t] \leq \frac{\VV[X]}{t^2}.
\end{equation*}
:::



:::{prf:theorem} Union Bound
Let $A_1, \ldots, A_m$ be a collection of events and let $A = A_1\cup \cdots \cup A_m$ be the union of these events (i.e. the event that anyone of the events occurs). 
Then
\begin{equation*}
\PP[A] \leq \sum_{i=1}^{m} \PP[A_i].
\end{equation*}
:::


## Properties of the expectation



:::{prf:theorem} Law of Total Expectation
Let $X$ and $Y$ be random variables. Then
\begin{equation*}
\EE[X] = \EE[\EE[X|Y]].
\end{equation*}
:::


:::{prf:theorem} Jensen's Inequality
Let $f$ be a convex function and $X$ be a random variable. Then
\begin{equation*}
f(\EE[X]) \leq \EE[f(X)].
\end{equation*}
:::

This implies that a bound on the expected squared error also gives a bound on the expected error.

### Matrix equations

Familiar facts about scalars also extend to matrices.

:::{prf:theorem} Bias-Variance Decomposition
:label: thm-bias-variance
Let $\vec{X}$ be a random matrix and $\vec{A}$ be a deterministic matrix. Then
\begin{equation*}
\EE[\|\vec{A} - \vec{X}\|_\F^2] = \|\vec{A} - \EE[\vec{X}]\|_\F^2 + \EE[\|\vec{X} - \EE[\vec{X}]\|_\F^2].
\end{equation*}
:::

:::{prf:theorem} Variance of iid sum
:label: thm-iid-sum
Let $\vec{X}_1, \ldots, \vec{X}_m$ be iid copies of $\vec{X}$. Then
\begin{equation*}
\VV\left[\left\|\frac{1}{m}\sum_{i=1}^m \vec{X}_i\right\|_\F^2\right] = \frac{1}{m}\VV[\|\vec{X}\|_\F^2].
\end{equation*}
:::


