# Trigonometric Sketching Matrices



````{prf:definition}
:label: def:trig-sketch
We say a matrix $\vec{S}\in\R^{k\times n}$ is a *trigonometric sketch* matrix if it has the distribution
```{math}
\vec{S} = \sqrt{\frac{n}{k}}\vec{R}\vec{F}\vec{E}\vec{\Pi},
```
where $\vec{R}$ is a restriction to $\vec{R}\in\R^{k\times n}$ random coordinates,  $\vec{F}\in\R^{n\times n}$ is a orthogonal fast trig transform (e.g. DCT), $\vec{E}\in\R^{n\times n}$ is a random sign flip, and $\vec{\Pi}\in\R^{n\times n}$ is a random permutation.
````

A trigonometric sketch matrix can be applied to $\vec{A}$ in $O(nd\log(n))$ operations.
A downside is that it is not easy to efficiently apply the sketch matrix to a sparse matrix $\vec{A}$.
In addition, parallelizing the application of tigonometric transforms is not as straightforward as for Gaussian or sparse sketches.

````{prf:theorem}

Fix any subspace $V\subset\R^n$ of dimension $d$.
Then, for any $0<\varepsilon<1$, the DCT trigonometric sketch matrix $\vec{S}$ is a subspace embedding for $V$ with constant distortion with high probability for some
```{math}
k = O\left(d\log(d)\right).
```
````

### Implementation

The implementation of a trigonometric sketch matrix is relatively straightforward.
An efficient application requires sequentially applying the constituent operations, and hence we define a custom class. 

````{code}
class trig_sketch():
    
    def __init__(self,n,k,rng):

        self.shape = (k,n)
        self.pi = rng.permutation(n)
        self.E = 2*rng.randint(0,2,n)-1
        self.R = rng.choice(n,size=k,replace=False)

    def __matmul__(self,A):

        A_loc = A.A if sp.sparse.issparse(A) else A
        return np.sqrt(self.shape[1]/self.shape[0])*sp.fft.dct(self.E[:,None]*A_loc[self.pi],norm='ortho',axis=0)[self.R]
````