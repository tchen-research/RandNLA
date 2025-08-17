# Sparse Sketching Matrices

Sparse sketching matrices aim to reduce the generate and apply times by making the sketching matrix sparse.


## CountSketch

The classical example of a sparse sketching matrix is the CountSketch matrix {cite:p}`clarkson_woodruff_13`.

````{prf:definition}
We say a matrix $\vec{S}\in\R^{k\times n}$ is a *CountSketch matrix* if it has the distribution
```{math}
\vec{S} = \begin{bmatrix}
\rho_1\vec{e}_{s_1} & \rho_2\vec{e}_{s_2} & \cdots & \rho_n\vec{e}_{s_n}
\end{bmatrix}
,\qquad
\begin{aligned}
&\rho_i\sim \Call{Rademacher}\text{ iid}\\
&s_i \sim \Call{Unif}(\{1,\ldots,k\})\text{ iid}.
\end{aligned}
```
````

A CountSketch matrix can be applied to $\vec{A}$ in $O(\nnz(\vec{A}))$ operations.

````{prf:theorem}

Fix any subspace $V\subset\R^n$ of dimension $d$.
Then, for any $0<\varepsilon<1$, the CountSketch matrix $\vec{S}$ is a subspace embedding for $V$ with distortion $\varepsilon$ with probability at least $1-\delta$ for some
```{math}
k = O\left( \frac{d^2}{\varepsilon^2\delta} \right).
```
````


## Sparse Stack Sketch

The poor scaling of embedding dimension in CountSketch can be remedied by increasing the per-column sparsity.
There are a number of ways to do this, but one of the most promising is to simply stack a bunch of independent CountSketch matrices on top of one another.


````{prf:definition}
:label: def:sparse-stack-sketch
We say a matrix $\vec{S}\in\R^{k\times n}$ is a *SparseStack matrix** if it has the distribution
```{math}
\vec{S} = \begin{bmatrix}
\rho_{1,1}\vec{e}_{s_{1,1}} & \rho_{1,2}\vec{e}_{s_{1,2}} & \cdots & \rho_{1,n}\vec{e}_{s_{1,n}} \\
\rho_{2,1}\vec{e}_{s_{2,1}} & \rho_{2,2}\vec{e}_{s_{2,2}} & \cdots & \rho_{2,n}\vec{e}_{s_{2,n}} \\
\vdots & \vdots & \ddots & \vdots \\
\rho_{\zeta,1}\vec{e}_{s_{\zeta,1}} & \rho_{\zeta,2}\vec{e}_{s_{\zeta,2}} & \cdots & \rho_{\zeta,n}\vec{e}_{s_{\zeta,n}}
\end{bmatrix}
,\qquad
\begin{aligned}
&\rho_{i,j}\sim \Call{Rademacher}\text{ iid}\\
&s_{i,j} \sim \Call{Unif}(\{1,\ldots,k/\zeta\})\text{ iid}.
\end{aligned}
```
````

This is equivalent to generating $\zeta$ CountSketch matrices of hight $k/\zeta$, and stacking them on top of one another.
A SparseStack matrix can be applied to $\vec{A}$ in $O(\zeta\nnz(\vec{A}))$ operations.

````{prf:theorem}

Fix any subspace $V\subset\R^n$ of dimension $d$.
Then, for any $0<\varepsilon<1$, the SparseStack matrix $\vec{S}$ is a subspace embedding for $V$ with distortion $\varepsilon$ with probability at least $1-\delta$ for some
```{math}
k = ?
,\quad
\zeta = ?.
```
````

### Implementation

It's relatively easy to efficiently generate SparseStack matrices in a high-level langauge like Python.

````{code}
def sparse_stack_sketch(n,k,zeta,rng):

    k_rem = k%zeta
    k_loc = k//zeta+(k_rem>0)

    C = np.random.randint(0,k_loc,size=(n,zeta))
    if k_rem > 0:
        C[:,-1] = np.random.randint(0,k_rem,size=n)
    C += np.arange(0,k,k_loc)

    indices = C.flatten()
    values = np.sqrt(1/zeta)*(2*np.random.randint(2,size=n*zeta)-1)
    indptr = np.arange(0,n+1)*zeta
    S = sp.sparse.csc_matrix ((values,indices,indptr),shape=(k,n))

    return S
````

### Comparison with sparse sign sketches

A perhaps more common sparse sketching distribution, typically called *SparseSign* matrix, does not block up the rows of the sketch.
Instead, each column has exactly $\zeta$ random signs in uniformly random positions.
This is somewhat more tedious to generate than SparseStack, but can be done efficiently with a bit of care.
Another bennefit of SparseStack is that the embedding dimension can easily be adjusted by stacking on more CountSketch matrices. 
This may be useful in practice, where an algorithm might need to adjust the embedding dimension on the fly.




