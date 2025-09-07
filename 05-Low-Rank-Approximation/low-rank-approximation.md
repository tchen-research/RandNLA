---
title: Low-Rank Approximation
description: Overview of randomized methods for low-rank matrix approximation including SVD, subspace iteration, and Nyström methods
keywords: [low-rank approximation, randomized SVD, subspace iteration, block Krylov, Nyström method, singular value decomposition, matrix compression]
numbering:
  equation:
    enumerator: 5.%s
  proof:theorem:
    enumerator: 5.%s
  proof:algorithm:
    enumerator: 5.%s
  proof:definition:
    enumerator: 5.%s
  proof:proposition:
    enumerator: 5.%s
  heading_2: false
---


:::{prf:definition} Low-rank Approximation
:label: task-low-rank
:enumerated: false
Given $\vec{A}\in\R^{n\times d}$ and $k\geq 0$, 
\begin{equation*}
\min_{\vec{B}\in\R^{n\times k},\vec{C}\in\R^{d\times k}} \|\vec{A}-\vec{B}\vec{C}^\T\|.
\end{equation*}
:::

It is well-known that the solution to {eq}`task-low-rank` can be obtained by computing the singular value decomposition (SVD) of $\vec{A}$.
In particular, if $\vec{A} = \vec{U} \vec{\Sigma} \vec{V}^\T$ is the SVD of $\vec{A}$, then the optimal low-rank approximation of rank $k$ is given by
\begin{equation}
\llbracket \vec{A} \rrbracket_k := \vec{U}_k \vec{\Sigma}_k \vec{V}_k^\T,
\end{equation}
where $\vec{U}_k$ contains the first $k$ columns of $\vec{U}$, $\vec{\Sigma}_k$ is the diagonal matrix containing the first $k$ singular values, and $\vec{V}_k$ contains the first $k$ columns of $\vec{V}$.

This chapter focuses on algorithms which work with matrices stored in memory. 
When reading individual entries of $\vec{A}$ is expensive, a related class of [sampling-based low-rank approximation](./low-rank-approximation-sampling) methods may be more appropriate. 
We discuss these methods along side other sampling-based methods in [Chapter 7](./sampling).



### Further reading

- @halko_martinsson_tropp_11: Early survey on the [Randomized SVD](./randomized-svd.ipynb) and [Randomized Subspace Iteration](./subspace-iteration.ipynb) that that popularized RandNLA for low-rank approximation.
- @musco_musco_15: First analysis of [Randomized Block Krylov Iteration](./block-krylov.ipynb)
- @tropp_webber_23: Recent explicit analysis of a number of low-rank approximation algorithms,
- @meyer_musco_musco_24, @chen_epperly_meyer_musco_rao_25: Line of work in TCS which study [Randomized Block Krylov Iteration](./block-krylov.ipynb) in the "small-block" setting (where the block size is smaller than the target rank).
