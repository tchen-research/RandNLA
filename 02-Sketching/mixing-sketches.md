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
Often such methods are *obvlious*, meaning the sketching distribution does not depend on the input matrix $\vec{A}$ (other than through the dimension).
The most common mixing-type sketching distributions are:

- [Gaussian](./Gaussian-sketch.md)
- [Sparse](./sparse-sketch.md)
- [Trigonometric](./trig-sketch.md)

Each have their own pros and cost (in theory and in practice). 
In the subsequent sections, we will introduce all of these methods. 
We then compare them head to head in [numerical experiments](./which-sketch-should-i-use.ipynb).