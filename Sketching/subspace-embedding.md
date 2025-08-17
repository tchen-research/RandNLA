# Subspace Embedding

Perhaps the most important property of a sketching matrix is that it preserves the geometry of a subspace.
This is quantified by the following definition: 

````{prf:definition} Subspace Embedding
:label: def-subspace-embedding

Let $V$ be a subspace of $\R^n$. We say a matrix $\vec{S}$ is a subspace embedding for $V$ with distortion $\varepsilon$ if
```{math}
\forall \vec{x}\in V: (1-\varepsilon)\|\vec{x}\| \leq \|\vec{S}\vec{x}\| \leq (1+\varepsilon)\|\vec{x}\|.
```
When $V = \range(\vec{A})$ for some matrix $\vec{A}$, we say that $\vec{S}$ is a subspace embedding for $\vec{A}$.
````

In particular, a subspace embedding ensures that the lengths of all vectors within a subspace are preserved by the sketch. 

## Equivalent Characterization

It will sometimes be useful to work with the following equivalent characterization of subspace embeddings:

````{prf:theorem}

Let $\vec{V}$ be an orthonormal basis for a subspace $V$ of $\R^n$. 
Then $\vec{S}$ is a subspace embedding for $V$ if and only if
```{math}
\| \vec{V}^\T \vec{S}^\T \vec{S} \vec{V} - \vec{I} \|_2 \leq \varepsilon.
```
````

````{admonition} Proof
:class: dropdown

TODO

````
