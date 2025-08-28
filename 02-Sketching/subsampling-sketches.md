---
title: Subsampling Sketches
description: Adaptive sketching methods that select important rows based on leverage scores and other importance measures
keywords: [subsampling sketches, adaptive sketching, leverage scores, row selection, importance sampling, sublinear algorithms]
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

## Subsampling Sketches

Subsampling-based sketching methods produce a sketch $\vec{S}\vec{A}$ where each row of the sketch is a scaling of single row of $\vec{A}$.
Typically these rows are selected based on their "importance", and hence the sketching distribution depends on the input matrix $\vec{A}$.
While not suitable for all settings, adaptive sketching offers the potential for *sublinear* algorithms (i.e. algorithms that run faster than it takes to look at every entry of the input).
The most common types of subsampling-based sketching distributions are:

- [Leverage scores](./leverage-scores.md)
- [Row norm sampling](./leverage-scores.md#Row-norm-sampling)

