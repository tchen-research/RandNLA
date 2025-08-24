---
title: Exact Factorization
description: Introduction to QR factorization algorithms for tall matrices including classical and randomized approaches
keywords: [QR factorization, Householder reflections, Givens rotations, SVD, numerical stability, factorization algorithms]
numbering:
  equation:
    enumerator: 3.%s
  proof:theorem:
    enumerator: 3.%s
  proof:algorithm:
    enumerator: 3.%s
  proof:definition:
    enumerator: 3.%s
  proof:proposition:
    enumerator: 3.%s
  heading_2: false
---

In this chapter we focus on algorithms for computing a QR factorization of a tall matrix $\vec{A}\in\R^{n\times d}$, where $n\gg d$.
:::{admonition} QR Factorization
:label: task-qr-factorization
Given $\vec{A}\in\R^{n\times d}$ (full rank), find a matrix $\vec{Q}\in\R^{n\times d}$ with orthonormal columns and an upper triangular matrix $\vec{R}\in\R^{d\times d}$ such that
\begin{equation*}
\vec{A} = \vec{Q}\vec{R}.
\end{equation*}
:::

The computational cost of a QR factorization is $O(nd^2)$ operations.
Classical algorithms for computing the QR factorization, such as the LAPACK methods underlying [`np.linalg.qr`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.qr.html), are typically based on Householder reflections or Givens rotations.
These algorithms are numerically stable, but inherently sequential, leading to relatively low flop-rates on modern hardware.
The algorithms presented in this chapter address this shortcoming.

## Other factorizations

Many of the ideas we discuss in this chapter can be used to compute a singular value decomposition (SVD). 
Alternately, on obtain an SVD decomposition of $\vec{A}$ efficiently from a QR factorization.
Simply compute an SVD $\vec{R} = \vec{U}' \vec{\Sigma} \vec{V}^\T$ and then set $\vec{U} = \vec{Q} \vec{U}'$ to obtain an SVD
\begin{equation*}
\vec{A} = \vec{U} \vec{\Sigma} \vec{V}^\T.
\end{equation*}



