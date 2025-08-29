---
title: Linear Regression
description: Overview of linear regression approaches including direct methods, iterative methods, and randomized algorithms
keywords: [linear regression, least squares, QR factorization, iterative methods, LSQR, LAPACK, numerical stability]
numbering:
  equation:
      enumerator: 4.%s
  proof:theorem:
      enumerator: 4.%s
  proof:algorithm:
      enumerator: 4.%s
  proof:definition:
      enumerator: 4.%s
  proof:proposition:
      enumerator: 4.%s
  heading_2: false
---


Linear regression is one of the core tasks in numerical linear algebra.

:::{prf:definition} Linear Regression
:label: task-regression
:enumerated: false
Given $\vec{A}\in\R^{n\times d}$ (full rank) and $\vec{b}\in\R^n$, solve
\begin{equation*}
\min_{\vec{x}\in\R^d} \|\vec{b}-\vec{A}\vec{x}\|.
\end{equation*}
:::

## Direct Methods

Classical direct solvers for {eq}`task-regression` such as the LAPACK method underlying [`np.linalg.lstsq`](https://numpy.org/devdocs/reference/generated/numpy.linalg.lstsq.html) work in two stages.
First, $\vec{A}$ is factorized (e.g QR factorization).
Second, the factorization is used to solve the linear system.
When implemented properly, such algorithms are numerically stable and require $O(nd^2)$ operations.

However, we identify two shortcomings of the above approach:.

- The dominant cost is computing a matrix factorization which, as we have seen in our discussion on the [cost of linear algebra](../01-Background/cost-of-numerical-linear-algebra.ipynb), does not have a particularly high flop-rate. 
- The total number of flops is $O(nd^2)$, which might be too expensive when $n\gg d \gg 1$.


## Iterative Methods

Iterative methods such as LSQR begin with an initial guess $\vec{x}_0$ and iteratively produce a sequence of approximate solutions $\vec{x}_1,\ldots,\vec{x}_t$, where ideally $\vec{x}_k$ is close to the solution of {eq}`task-regression`.
At each iteration, such methods perform a matrix-vector product with $\vec{A}$ and $\vec{A}^\T$, in addition to some vector operations.
Thus, the matrix-vector products are typically the dominant cost, and require $O(\nnz(\vec{A})) \leq O(nd)$ operations per iteration. 
While iterative methods are able to take advantage of sparsity in $\vec{A}$, they may require many iterations to converge when $\vec{A}$ is ill-conditioned problems.

## Further Reading

- @sarlos_06, @rokhlin_tygert_08: Early works in RandNLA that respectively introduce [sketch-and-solve](./sketch-and-solve.ipynb) and [sketch-and-precondition](./sketch-and-precondition.ipynb).
- @clarkson_woodruff_13, @chenakkod_derezinski_dong_rudelson_24,@chenakkod_derezinski_dong_25: Line of work in TCS on sparse sketches that give algorithms for regression that run in time close to the optimal $O(\nnz(\vec{A}) + d^{\omega})$. 
- @epperly_24, @epperly_meier_nakatsukasa_25: Line of work on the stability fo sketch-and-precondition type algorithms
