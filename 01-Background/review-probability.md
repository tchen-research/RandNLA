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



## Properties of the expectation


The expectation operator has several useful properties that are frequently used in the analysis of randomized algorithms.

The first is the law of total expectation, which is useful for accounting for separate sources of randomness separately.

:::{prf:theorem} Law of Total Expectation
Let $X$ and $Y$ be random variables. Then
\begin{equation*}
\EE[X] = \EE[\EE[X|Y]].
\end{equation*}
:::

<!-- 
Another useful fact is Jensen's inequality.
:::{prf:theorem} Jensen's Inequality
Let $f$ be a convex function and $X$ be a random variable. Then
\begin{equation*}
f(\EE[X]) \leq \EE[f(X)].
\end{equation*}
:::
This implies that a bound on the expected squared error also gives a bound on the expected error. -->


### Matrix equations

Familiar facts about scalars also extend to matrices. The following results are particularly useful for analyzing the performance of randomized matrix algorithms.

:::{prf:theorem} Bias-Variance Decomposition
:label: thm-bias-variance
Let $\vec{X}$ be a random matrix and $\vec{A}$ be a deterministic matrix. Then
\begin{equation*}
\EE[\|\vec{A} - \vec{X}\|_\F^2] = \|\vec{A} - \EE[\vec{X}]\|_\F^2 + \EE[\|\vec{X} - \EE[\vec{X}]\|_\F^2].
\end{equation*}
:::

:::{prf:proof}
:class: dropdown
:enumerated: false
We use the algebraic identity $(a-b)^2 = (a-c)^2 + (c-b)^2 + 2(a-c)(c-b)$ with $a = \vec{A}$, $b = \vec{X}$, and $c = \EE[\vec{X}]$:
\begin{equation*}
\|\vec{A} - \vec{X}\|_\F^2 &= \|\vec{A} - \EE[\vec{X}]\|_\F^2 + \|\EE[\vec{X}] - \vec{X}\|_\F^2 + 2\langle\vec{A} - \EE[\vec{X}], \EE[\vec{X}] - \vec{X}\rangle_\F,
\end{equation*}
where $\langle \vec{X},\vec{Y}\rangle_\F := \tr(\vec{X}^\T\vec{Y})$.
Next, by the linearity of expectation,
\begin{equation*}
\begin{aligned}
\EE\left[ \langle\vec{A} - \EE[\vec{X}], \EE[\vec{X}] - \vec{X}\rangle_\F \right]
&= 
\langle\vec{A} - \EE[\vec{X}], \EE[\EE[\vec{X}] - \vec{X}]\rangle_\F 
\\&=
\langle\vec{A} - \EE[\vec{X}], \EE[\vec{X}] - \EE[\vec{X}]\rangle_\F 
\\&= 0.
\end{aligned}
\end{equation*}
The result follows by taking the expectation.
:::

We can define the variance of a random matrix similar to the variance of a random scalar.
:::{prf:definition}
:label: def-variance
Let $\vec{X}$ be a random matrix. We define
\begin{equation*}
\VV[\vec{X}] := \EE\left[ \|\vec{X} - \EE[\vec{X}] \|_\F^2\right].
\end{equation*}
:::

The bias-variance decomposition shows that the error of any estimator can be separated into systematic bias and random variance components.

In many RandNLA algorithms, we average iid copies of a random matrix estimator to reduce variance. 
Similar to the scalar case, the variance decreases proportional to the number of copies averaged.

:::{prf:theorem} Variance of iid sum
:label: thm-iid-sum
Let $\vec{X}_1, \ldots, \vec{X}_m$ be iid copies of $\vec{X}$. Then
\begin{equation*}
\VV\left[\frac{1}{m}\sum_{i=1}^m \vec{X}_i\right] = \frac{1}{m}\VV[\vec{X}].
\end{equation*}
:::

:::{prf:proof}
:class: dropdown
:enumerated: false

By [](thm-bias-variance) and [](def-variance), without loss of generality, we can assume $\EE[\vec{X}] = \vec{0}$.
Then, expanding and using linearity of expectation and that $\vec{X}_i$ and $\vec{X}_j$ are independent (if $i\neq j$).
\begin{equation*}
\begin{aligned}
\VV\left[\frac{1}{m}\sum_{i=1}^m \vec{X}_i\right] 
&=
\EE\left[ \left\| \frac{1}{m} \sum_{i=1}^{m} \vec{X}_i \right\|_\F^2 \right]
\\&= \frac{1}{m^2} \sum_{i=1}^{m} \sum_{j=1}^{m} \EE[\langle\vec{X}_i,\vec{X}_j\rangle_\F].
\\&= \frac{1}{m^2} \sum_{i=1}^{m} \EE[\|\vec{X}_i\|_\F^2].
\\&= \frac{1}{m} \EE[\|\vec{X}\|_\F^2]
\\&= \VV[\vec{X}].
\end{aligned}
\end{equation*}

:::



## Properties of probability

We sometimes work with probabilties. 


:::{prf:theorem} Union Bound
Let $A_1, \ldots, A_m$ be a collection of events and let $A = A_1\cup \cdots \cup A_m$ be the union of these events (i.e. the event that anyone of the events occurs). 
Then
\begin{equation*}
\PP[A] \leq \sum_{i=1}^{m} \PP[A_i].
\end{equation*}
:::

:::{prf:theorem} Law of Total Probability
Let $A$ be an event and $B_1, B_2, \ldots, B_n$ be a partition of the sample space (i.e., mutually exclusive events whose union is the entire space). Then
\begin{equation*}
\PP[A] = \sum_{i=1}^n \PP[A|B_i] \PP[B_i].
\end{equation*}
:::

### Concentration inequalities

Concentration inequalities tell us how close a random variable is to some value. 
The most basic concentration inequality is Markov's.

:::{prf:theorem} Markov's Inequality
Let $X$ be a non-negative random variable. 
Then
\begin{equation*}
\PP[X\geq t] \leq \frac{\EE[X]}{t}.
\end{equation*}
:::

:::{prf:proof}
:class: dropdown
:enumerated: false
Let $f_X(x)$ be the density of $X$.
We have
\begin{equation*}
\begin{aligned}
\EE[X] &= \int_0^\infty x f_X(x) \, \d{x} \\
&= \int_0^t x f_X(x) \, \d{x} + \int_t^\infty x f_X(x) \, \d{x} \\
&\geq \int_t^\infty x f_X(x) \, \d{x} \\
&\geq t \int_t^\infty f_X(x) \, \d{x} \\
&= t \PP[X \geq t].
\end{aligned}
\end{equation*}
Rearranging gives the result.
:::

Markov's inequality implies that a random variable is unlikely to be far from its mean (relative to the variance).

:::{prf:theorem} Chebyshev's Inequality
Let $X$ be a random variable. 
Then
\begin{equation*}
\PP[|X - \EE[X]| \geq t] \leq \frac{\VV[X]}{t^2}.
\end{equation*}
:::


:::{prf:proof}
:class: dropdown
:enumerated: false

Apply Markov to $(\vec{X} - \EE[\vec{X}])^2$.

:::

There are many other concentration inequalities (e.g. [Bernstein](https://en.wikipedia.org/wiki/Bernstein_inequalities_(probability_theory)), [Chernoff](https://en.wikipedia.org/wiki/Chernoff_bound), [Hoeffding](https://en.wikipedia.org/wiki/Hoeffding%27s_inequality), etc.), which provide better dependence on $t$ for "nice" random variables.
Such bounds are used in many RandNLA analyses, but will not be particularly important in this book.


