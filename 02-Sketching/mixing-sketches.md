---
title: Mixing Sketches
description: Overview of mixing-based sketching methods including Gaussian, sparse, and trigonometric approaches
keywords: [mixing sketches, oblivious sketching, Gaussian sketch, sparse sketch, trigonometric sketch, linear combinations]
numbering:
  equation:
    enumerator: 2.%s
    continue: true
  proof:theorem:
    enumerator: 2.%s
    continue: true
  proof:algorithm:
    enumerator: 2.%s
    continue: true
  proof:definition:
    enumerator: 2.%s
    continue: true
  proof:proposition:
    enumerator: 2.%s
    continue: true
---

## Mixing Sketches

Mixing-based sketching methods produce a sketch $\vec{S}\vec{A}$ where each row of the sketch is a linear combination of multiple rows of $\vec{A}$.
Often such methods are *obvlious*, meaning the sketching distribution works for any fixed subspace of the given dimension.
The most common mixing-type sketching distributions are:

- [Gaussian](./Gaussian-sketch.ipynb)
- [Sparse](./sparse-sketch.ipynb)
- [Trigonometric](./trig-sketch.ipynb)

Gaussian sketches can be viewed as the prototypical sketching distribution. 
Since the Gaussian distribution is so nice to work with, it's often easiest to analyze RandNLA algorithms that use Gaussian sketches. 
However, generating an applying Gaussian sketching matrices is expensive.

To reduce the cost of generating and applying the sketching matrix, it is common to use structured sketches.
Common examples include using sparsity or fast trigonometric transforms (e.g. FFT).
Remarkably, the mathematical behavior of these structured sketching distributions is often very similar to Gaussian sketches, so any intuition we build from analyses of algorithms based on Gaussian sketches typicaly extends to these structured sketches too.


In the subsequent sections, we will introduce all of these methods in detail. 
We then compare them head to head in [numerical experiments](./which-sketch-should-i-use.ipynb).