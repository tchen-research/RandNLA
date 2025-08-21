#  Linear Regression


Linear regression is one of the core tasks in numerical linear algebra.
Concretely, we wish to solve the minimization problem:
```{math}
:label: eqn-regression
\min_{\vec{x}\in\R^d} \|\vec{b}-\vec{A}\vec{x}\|
,\qquad \vec{A}\in\R^{n\times d}, \quad \vec{b}\in\R^n.
```
For convenience, we will assume that $\vec{A}$ is full-rank.

<h2>Direct Methods</h2>

Classical direct solvers for {eq}`eqn-regression` such as the LAPACK method underlying [`np.linalg.lstsq`](https://numpy.org/devdocs/reference/generated/numpy.linalg.lstsq.html) work in two stages.
First, $\vec{A}$ is factorized (e.g QR factorization).
Second, the factorization is used to solve the linear system.
When implemented properly, such algorithms are numerically stable and require $O(nd^2)$ operations.

However, we identify two shortcomings of the above approach:.

- The dominant cost is computing a matrix factorization which, as we have seen in our discussion on the [cost of linear algebra](../Background/cost-of-numerical-linear-algebra.ipynb), does not have a particularly high flop-rate. 
- The total number of flops is $O(nd^2)$, which might be too expensive when $n\gg d \gg 1$.


<h2>Iterative Methods</h2>

Iterative methods such as LSQR begin with an initial guess $\vec{x}_0$ and iteratively produce a sequence of approximate solutions $\vec{x}_1,\ldots,\vec{x}_t$, where ideally $\vec{x}_k$ is close to the solution of {eq}`eqn-regression`.
At each iteration, such methods perform a matrix-vector product with $\vec{A}$ and $\vec{A}^\T$, in addition to some vector operations.
Thus, the matrix-vector products are typically the dominant cost, and require $O(\nnz(\vec{A})) \leq O(nd)$ operations per iteration. 
While iterative methods are able to take advantage of sparsity in $\vec{A}$, they may require many iterations to converge when $\vec{A}$ is ill-conditioned problems.
