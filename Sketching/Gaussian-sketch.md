# Gaussian Sketching Matrices



````{prf:definition} Gaussian Matrix
We say a matrix $\vec{G} \in \R^{p \times q}$ is a Gaussian matrix if its entries are independent and identically distributed random variables drawn from a standard normal distribution $\mathcal{N}(0,1)$.
````


````{code}
def gaussian_sketch(n,k,rng):
    S = rng.randn(k,n) / np.sqrt(k)
    return S
````
[Numerical Experiments](./which-sketch-should-i-use.ipynb)


### Orthogonal Invariance

````{prf:proposition} Orthogonal Invariance
Let $\vec{G} \sim \operatorname{Gaussian}(p,q)$ be a Gaussian matrix. 
Then, for any compatible orthogonal matrix $\vec{Q}$,
```{math}
\vec{Q} \vec{G} \sim \operatorname{Gaussian}(p,q).
```
````

### Spectral Properties

````{prf:proposition} Eigenvalue bounds
````

````{prf:theorem} Gaussian Subspace Embedding
````


### Other properties

{cite:p}`tropp_webber_23`


````{prf:proposition}
Let $\vec{G} \sim \operatorname{Gaussian}(p,q)$. 
Then, for compatible matrices $\vec{X}$ and $\vec{Y}$, 
```{math}
    \EE\bigl[ \| \vec{X} \vec{G} \vec{Y} \|_\F^2 \bigr]
    = \| \vec{X} \|_\F^2 \|\vec{Y}\|_\F^2.        
```
Moreover, if $p-q \geq 2$, then 
```{math}
\EE\bigl[ \| \vec{G}^\dagger \|_\F^2 \bigr]
= \frac{q}{p-q-1}.
```
````
