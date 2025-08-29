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






\begin{equation*}
\EE[\|\EE[\vec{X}] - \vec{X}\|_\F^2]
\end{equation*}

