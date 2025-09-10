---
title: Numerical Linear Algebra
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


## Matrices 

It is often useful to think of a matrix-vector product can be though of as a linear combination of the columns of the matrix. 
That is,
\begin{equation*}
\begin{bmatrix}
| & & |\\
\vec{a}_1 & \cdots & \vec{a}_d\\
| & & |
\end{bmatrix}
\begin{bmatrix} 
x_1 \\ \vdots \\ x_d \end{bmatrix} 
= x_1 \vec{a}_1 + \cdots + x_d \vec{a}_d.
\end{equation*}


## Norms

:::{prf:theorem}
:label: thm-l2-l1
\begin{equation*}
\| \vec{x} \|_2 \leq \|\vec{x}\|_1 \leq \sqrt{n} \|\vec{x}\|_2
\end{equation*}
:::


## Factorizations

:::{prf:definition}
A Cholesky factorization of a symmetric positive definite matrix $\vec{A} \in \R^{n \times n}$ is a decomposition
\begin{equation*}
\vec{A} = \vec{R}^\T \vec{R}
\end{equation*}
where $\vec{R} \in \R^{n \times n}$ is upper-triangular with positive diagonal entries.
:::

:::{prf:definition}
A QR decomposition of a matrix $\vec{A} \in \R^{n \times d}$ is a factorization 
\begin{equation*}
\vec{A} = \vec{Q} \vec{R}
\end{equation*}
where $\vec{Q} \in \R^{n \times d}$ has orthonormal columns ($\vec{Q}^\T \vec{Q} = \vec{I}$) and $\vec{R} \in \R^{d \times d}$ is upper triangular.
:::


:::{prf:definition}
An singular value is a decomposition (SVD) of a matrix $\vec{A} \in \R^{n \times d}$ (wlog $n\geq d$) is a factorization
\begin{equation*}
\vec{A} = \vec{U} \vec{\Sigma} \vec{V}^\T 
= \sum_{i=1}^{d} \sigma_i \vec{u}_i \vec{v}_i^\T,
\end{equation*}
where $\vec{U} \in \R^{n \times d}$ has orthonormal columns $\vec{u}_i$, $\vec{V} \in \R^{d \times d}$ has orthonormal columns $\vec{v}_i$, and $\vec{\Sigma} \in \R^{d \times d}$ is diagonal with non-negative entries $\sigma_1 \geq \cdots \geq \sigma_d \geq 0$.
:::


The above definition is sometimes called a reduced or thin SVD. 
By extending $\vec{U}$ to an orthonormal basis for $\R^n$ and appending zeros below $\vec{\Sigma}$ we obtain a full SVD.

The SVD provides the best low-rank approximation to a matrix.
:::{prf:theorem}
If $\vec{A} = \vec{U} \vec{\Sigma} \vec{V}^\T$ is the SVD of $\vec{A}$, then the best rank-$k$ approximation to $\vec{A}$ in any orthogonal invariant norm is given by
\begin{equation*}
\llbracket\vec{A}\rrbracket_k := \vec{U}_k \vec{\Sigma}_k \vec{V}_k^\T
= \sum_{i=1}^{k} \sigma_i \vec{u}_i \vec{v}_i^\T,
\end{equation*}
where $\vec{U}_k$ is the first $k$ columns of $\vec{U}$, $\vec{\Sigma}_k$ is the top-left $k\times k$ submatrix of $\vec{\Sigma}$, and $\vec{V}_k$ is the first $k$ columns of $\vec{V}$.
:::

:::{prf:definition}
An eigendecomposition of a symmetric matrix $\vec{A} \in \R^{n \times n}$ is a factorization
\begin{equation*}
\vec{A} = \vec{U} \vec{\Lambda} \vec{U}^\T
= \sum_{i=1}^{n} \lambda_i \vec{u}_i \vec{u}_i^\T
\end{equation*}
where $\vec{U} \in \R^{n \times n}$ has orthonormal columns $\vec{u}_i$ and $\vec{\Lambda} \in \R^{n \times }n$ is diagonal with entries $\lambda_1, \ldots, \lambda_n$.
:::


## Conditioning 

A problem/task is said to be *well-conditioned* if small perturbations in problem don't change the solution by much. 
If a small change to the problem can cause a large change in the solution, then the problem is said to be *ill-conditioned*.
Ill-conditioned problems are difficult (or impossible) to solve accurately  on computers, since even small errors made representing the problem on a computer can drastically change the solution.

In numerical linear algebra the *condition-number* of a matrix $\vec{A}$ is defined as
\begin{equation*}
\cond(\vec{A}) := \frac{\smax(\vec{A})}{\smin(\vec{A})},
\end{equation*}
where $\smax(\vec{A})$ and $\smin(\vec{A})$ are the largest and smallest singular values of $\vec{A}$, respectively.
The conditioning of many core linear algebra tasks depends on the condition number.


## The Lanczos Method for Matrix Functions

Let $\vec{A}\in\R^{n\times n}$ be a symmetric matrix with eigendecomposition $\vec{A} = \sum_{i=1}^{n} \lambda_i \vec{u}_i \vec{u}_i^\T$, where $\lambda_i$ are the eigenvalues and $\vec{u}_i$ are the orthonormal eigenvectors of $\vec{A}$.
Recall the matrix function corresponding to $\vec{A}$ and $f:\R\to\R$ is defined as
\begin{equation*}
f(\vec{A}) := \sum_{i=1}^{n} f(\lambda_i) \vec{u}_i \vec{u}_i^\T.
\end{equation*}

The Lanczos method can be used to approximate the maps $\vec{x}\mapsto \vec{x}^\T f(\vec{A})\vec{x}$ and $\vec{x}\mapsto f(\vec{A})\vec{x}$.

:::{prf:definition} Krylov Subspace
Given a matrix $\vec{A}\in\R^{n\times n}$ and a vector $\vec{x}\in\R^n$, the *Krylov subspace* of order $k$ is defined as
\begin{equation*}
\mathcal{K}_k(\vec{A}, \vec{x}) := \text{span}\{\vec{x}, \vec{A}\vec{x}, \ldots, \vec{A}^{k-1}\vec{x}\}.
\end{equation*}
:::

When applied to a symmetric matrix $\vec{A}$ for $k$ iterations, the [Lanczos algorithm](https://en.wikipedia.org/wiki/Lanczos_algorithm) produces an orthonormal basis $\vec{Q}\in\R^{n\times k}$ for the Krylov subspace $\mathcal{K}_k(\vec{A}, \vec{x})$ and a symmetric tridiagonal matrix $\vec{T}\in\R^{k\times k}$ such that $\vec{T} = \vec{Q}^\T\vec{A}\vec{Q}$.