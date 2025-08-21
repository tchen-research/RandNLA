---
title: Leverage Score Sketching
description: Leverage score-based subsampling for matrix sketching including definitions, properties, and applications
keywords: [leverage scores, leverage score sampling, subspace embedding, matrix sketching, row importance, approximate matrix multiplication]
---

## Leverage Score Sketching


````{prf:definition}
The $i$th leverage score of subspace $V\subset\R^n$ is defined as
```{math}
\ell_i := \| \vec{e}_i^\T \vec{V} \|^2,
```
where $\vec{V}$ is any orthonormal basis for $V$.
````


````{prf:definition}
:label: def:sparse-stack-sketch
We say a matrix $\vec{S}\in\R^{k\times n}$ is a *Leverage Score sampling matrix* if it has the distribution
```{math}
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
```
````
Here $\Call{leverage-dist}(\vec{A})$ is the distribution on $\{1,\ldots,n\}$ that samples each index $i$ with probability proportional to the leverage score $\ell_i$ of the $i$th column of $\vec{A}$.

Note that applying the Leverage score sampling matrix amounts to extracting rows, and therefore $\vec{S}$ can be applied to matrices and vectors *without reading the whole input*.

## Subspace Embedding

Leverage score sampling gives a subspace embedding:
````{prf:theorem} 
Fix any subspace $V\subset\R^n$ of dimension $d$.
Then, for any $0<\varepsilon<1$, the Leverage score sketching matrix $\vec{S}$ is a subspace embedding for $V$ with distortion $\varepsilon$ with probability at least $1-\delta$ for some
```{math}
k = O\left( \frac{d \log(d/\delta)}{\varepsilon^2} \right).
```
````

A nice proof of this can be found on Raphael's [wiki](https://randnla.github.io/leverage-subspace-embedding/).

## Approximate Matrix Multiplication