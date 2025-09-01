---
title: Sketching
description: Introduction to sketching techniques in randomized numerical linear algebra, covering mixing and subsampling approaches for matrix approximation.
keywords: [sketching, matrix sketching, subspace embedding, mixing sketches, subsampling, dimensionality reduction, random projections]
numbering:
  equation:
    enumerator: 2.%s
  proof:theorem:
    enumerator: 2.%s
  proof:algorithm:
    enumerator: 2.%s
  proof:definition:
    enumerator: 2.%s
  proof:proposition:
    enumerator: 2.%s
---




The workhorse of RandNLA is a technique called *sketching*.[^linear-sketch]
Sketching is a way to take a large matrix and create a smaller matrix (called a sketch) that approximates key properties of the original matrix.
Which properties are approximated depends on the specific sketching method used, and the application at hand.

[^linear-sketch]: In RandNLA, sketching is almost always done using a linear transform of the original matrix.

:::{sidebar} Like in drawing
This is like how a [sketch](./https://en.wikipedia.org/wiki/Sketch_(drawing)) captures the essence of an original image without all the details.
![Historical sketch drawing showing simplified lines capturing the essence of a detailed scene](https://upload.wikimedia.org/wikipedia/commons/3/32/Jesus_und_Ehebrecherin.jpg)
:::

:::{image} ./sketch_def.svg
:class: dark:hidden
:alt: Diagram showing matrix sketching process: an n×d input matrix A is multiplied by a k×d sketching matrix S to produce a smaller k×d sketch SA, where k is much smaller than n
:::

:::{image} ./sketch_def-dark.svg
:class: hidden dark:block
:alt: Diagram showing matrix sketching process: an n×d input matrix A is multiplied by a k×d sketching matrix S to produce a smaller k×d sketch SA, where k is much smaller than n
:::


An example of sketching is illustrated above. 
Here a sketching matrix $\vec{S}$ with *sketching/embedding dimension* $k$ is applied to a $n\times d$ input matrix $\vec{A}$.
The resulting $k\times d$ sketch $\vec{S}\vec{A}$ is much smaller than the original matrix.

When choosing a sketching distribution, two important considerations are:
- How fast the sketching matrix can be generated and applied to $\vec{A}$,
- How well the sketch $\vec{S}\vec{A}$ approximates the original matrix $\vec{A}$.

While these two considerations are often at odds with each other, by choosing the sketch at random from a suitable distribution, we can often achieve a good balance between the two.
In fact, in many algorithms in RandNLA, the randomness in the sketching matrix is the only source of randomness in the entire problem, and is only needed to ensure the above two considerations.


In this book, we treat sketches that [mix](./mixing-sketches.md) the rows of $\vec{A}$ and sketches that  [subsample](./subsampling-sketches.md) the rows of $\vec{A}$ as conceptually different.
We primarily focus on algorithms based on mixing-based sketches, since these tend to be most suitable as a default choice algorithm in many settings. 
We discuss subsampling-based methods, which can provide substantial speedups in certain contexts, in the chapter on [](../07-Sampling-Based-Methods/intro.md).
