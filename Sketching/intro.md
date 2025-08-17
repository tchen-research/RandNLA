# Sketching


The workhorse of RandNLA is a technique called *sketching*. 
Sketching is a way to take a large matrix and create a smaller matrix (called a sketch) that approximates key properties of the original matrix.[^sketch]
In RandNLA, sketching is almost always done using a linear transform of the original matrix.

![](./sketch_def.svg)


[^sketch]: This is like how a sketch captures the essence of an original image without all the details.

Many sketching methods can be categorized by whether they mix the rows of $\vec{A}$ together or subsample them.

<h2>Mixing based sketching</h2>

Mixing-based sketching methods produce a sketch $\vec{S}\vec{A}$ where each row of the sketch is a linear combination of multiple rows of $\vec{A}$.
Often such methods are *obvlious*, meaning the sketching distribution does not depend on the input matrix $\vec{A}$ (other than through the dimension).
The most common mixing-type sketching distributions are:

- [Gaussian](./Gaussian-sketch.md)
- [Sparse](./sparse-sketch.md)
- [Trigonometric](./trig-sketch.md)

Each have their own pros and cost (in theory and in practice). 
In the subsequent sections, we will introduce all of these methods. 
We then compare them head to head in [numerical experiments](./which-sketch-should-i-use.ipynb).

<h2>Subsampling based sketching</h2>

Subsampling-based sketching methods produce a sketch $\vec{S}\vec{A}$ where each row of the sketch is a scaling of single row of $\vec{A}$.
Typically these rows are selected based on their "importance", and hence the sketching distribution depends on the input matrix $\vec{A}$.
While not suitable for all settings, adaptive sketching offers the potential for *sublinear* algorithms (i.e. algorithms that run faster than it takes to look at every entry of the input).
The most common types of subsampling-based sketching distributions are:

- [Leverage scores](./leverage-scores.md)
- Row norm sampling

