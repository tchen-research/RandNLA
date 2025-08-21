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
---

## Low-Rank Approximation

Low-rank approximation is a fundamental problem in numerical linear algebra 


:::{admonition} Low-rank Approximation
:label: task-low-rank
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

