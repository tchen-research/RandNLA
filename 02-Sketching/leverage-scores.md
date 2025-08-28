---
title: Leverage Score Sketching
description: Leverage score-based subsampling for matrix sketching including definitions, properties, and applications
keywords: [leverage scores, leverage score sampling, subspace embedding, matrix sketching, row importance, approximate matrix multiplication]
numbering:
  equation:
    enumerator: 2.%s
    continue: true
  proof:theorem:
    enumerator: 2.%s
    continue: true
  proof:algorithm:
    enumerator: 2.%s
    continue: true
  proof:definition:
    enumerator: 2.%s
    continue: true
  proof:proposition:
    enumerator: 2.%s
    continue: true
---


:::{prf:definition}
:label: def:leverage-score
The $i$th leverage score of subspace $V\subset\R^n$ is defined as
\begin{equation*}
\ell_i := \| \vec{e}_i^\T \vec{V} \|^2,
\end{equation*}
where $\vec{V}$ is any orthonormal basis for $V$.
:::


:::{prf:definition}
:label: def:leverage-score-sketch
We say a matrix $\vec{S}\in\R^{k\times n}$ is a *Leverage Score sampling matrix* if it has the distribution
\begin{equation*}
\vec{S} = \begin{bmatrix}
-&\rho_1\vec{e}_{s_1}^\T&- \\
-&\rho_2\vec{e}_{s_2}^\T&- \\
&\vdots  \\
-&\rho_n\vec{e}_{s_n}^\T&-
\end{bmatrix}
,\qquad
\begin{aligned}
&s_{i} \sim \Call{leverage-dist}(\vec{A}),\\
&\rho_{i} = 1/\sqrt{d/(k\ell_{s_i})}.
\end{aligned}
\end{equation*}
:::
Here $\Call{leverage-dist}(\vec{A})$ is the distribution on $\{1,\ldots,n\}$ that samples each index $i$ with probability proportional to the leverage score $\ell_i$ of the $i$th column of $\vec{A}$.

Note that applying the Leverage score sampling matrix amounts to extracting rows, and therefore $\vec{S}$ can be applied to matrices and vectors *without reading the whole input*.

## Subspace Embedding

Leverage score sampling gives a subspace embedding:
:::{prf:theorem} 
:label: prf-leverage-SE
Fix any subspace $V\subset\R^n$ of dimension $d$.
Then, for any $0<\varepsilon<1$, the Leverage score sketching matrix $\vec{S}$ is a subspace embedding for $V$ with distortion $\varepsilon$ with probability at least $1-\delta$ for some
\begin{equation*}
k = O\left( \frac{d \log(d/\delta)}{\varepsilon^2} \right).
\end{equation*}
:::

A nice proof of this can be found on Raphael's [wiki](https://randnla.github.io/leverage-subspace-embedding/).

## Approximate Leverage-scores

Many of the facts about leverage-score sketching (e.g. {prf:ref}`prf-leverage-SE`) can be extended to arbitrary probability distributions.
In this case, what matters is how close the sampling distribution is to the leverage score distribution. 

:::{prf:theorem} 
:label: prf-leverage-SE-approx

Suppose we have approximate leverage scores $\tilde{\ell}_i$ satisfying $c_{\textup{min}} \tilde{\ell}_i \leq \ell_i \leq c_{\textup{max}} \tilde{\ell}_i$ for all $i$. 
Fix any subspace $V\subset\R^n$ of dimension $d$.
Then, for any $0<\varepsilon<1$, the approximate Leverage score sketching matrix $\vec{S}$ is a subspace embedding for $V$ with distortion $\varepsilon$ with probability at least $1-\delta$ for some
\begin{equation*}
k = O\left( \frac{(c_{\textup{max}}/c_{\textup{min}}) d \log(d/\delta)}{\varepsilon^2} \right).
\end{equation*}
:::


### Row-norm sampling

As an example, consider row-norm sampling, where we sample proportional to $r_i := \| \vec{e}_i^\T \vec{A} \|^2$ for some matrix $\vec{A}$.
Row-norms are a common way of measuring the "importance" of rows of a matrix. 

Let $\vec{V}\vec{R} = \vec{A}$ be a QR decomposition of $\vec{A}$. 
Then
```{math}
r_i = \| \vec{e}_i \vec{A} \|^2
= \|\vec{e}_i \vec{V} \vec{R} \|^2.
```
Then, since $\|\vec{R}\| = \smax(\vec{A})$ and $\|\vec{R}^{-1}\| = \smin(\vec{A})\|$, we find that
```{math}
\ell_i \smin(\vec{A})^2 \leq r_i \leq \ell_i \smax(\vec{A})^2.
```
This demonstrated that, we can use row-norm sampling in place of leverage score sampling, at the cost of paying for the conditioning of the matrix $\vec{A}$.


This highlights an important fact: *row-norm sampling is basis dependent*.
On the other hand, many tasks where we might used row-norm sampling are basis independent, and instead just depend on the relevant subspace. 
In such cases, one should think twice about using row-norm sampling.  