#  Regression


Linear regression is one of the core tasks in numerical linear algebra.
Concretely, we wish to solve the minimization problem:
```{math}
:label: eqn-regression
\min_{\vec{x}\in\R^d} \|\vec{b}-\vec{A}\vec{x}\|
,\qquad \vec{A}\in\R^{n\times d}, \quad \vec{b}\in\R^n.
```

Classical solvers for {eq}`eqn-regression` such as the LAPACK method underlying [`np.linalg.lstsq`](https://numpy.org/devdocs/reference/generated/numpy.linalg.lstsq.html) work in two stages.
First, $\vec{A}$ is factorized (e.g QR factorization).
Second, the factorization is used to solve the linear system.
In {prf:ref}`least-squares-qr`, we give pseudocode for a standard QR-based algorithm for solving linear regression using a QR factorization.

```{prf:algorithm} Least Squares by QR
:label: least-squares-qr

**Input:** $\vec{A}\in\R^{n\times d}$, $\vec{b}\in\R^n$

1. Factor $\vec{A} = \vec{Q} \vec{R}$ using a QR factorization algorithm
1. Solve $\vec{R}\vec{x} = \vec{Q}^\T \vec{b}$ using triangular solver

**Output:** $\vec{x}$
```

When implemented properly, the above algorithm is stable and accurate.
The cost of the algorithm is dominated by step 1, which requires $O(nd^2)$ operations.

We identify two shortcomings of the above algorithm that can each be addressed through the use of randomization.

- The dominant cost is computing a matrix factorization which, as we have seen in our discussion on the [cost of linear algebra](../Background/cost-of-numerical-linear-algebra.ipynb), does not have a particularly high flop-rate. 
- The total number of flops is $O(nd^2)$, which might be too expensive when $n\gg d \gg 1$.



## Table of Concents

```{tableofcontents}
```





