# Subsampling Sketches

Subsampling-based sketching methods produce a sketch $\vec{S}\vec{A}$ where each row of the sketch is a scaling of single row of $\vec{A}$.
Typically these rows are selected based on their "importance", and hence the sketching distribution depends on the input matrix $\vec{A}$.
While not suitable for all settings, adaptive sketching offers the potential for *sublinear* algorithms (i.e. algorithms that run faster than it takes to look at every entry of the input).
The most common types of subsampling-based sketching distributions are:

- [Leverage scores](./leverage-scores.md)
- Row norm sampling

