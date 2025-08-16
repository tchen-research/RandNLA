#  QR Factorization


QR factorization is one of the fundamental matrix decompositions in numerical linear algebra.
For a matrix $\vec{A} \in \R^{n \times d}$, a QR factorization is a decomposition 
```{math}
:label: eqn-qr-factorization
\vec{A} = \vec{Q} \vec{R}
```
where $\vec{Q} \in \R^{n \times d}$ has orthonormal columns ($\vec{Q}^\T \vec{Q} = \vec{I}$) and $\vec{R} \in \R^{d \times d}$ is upper triangular.

The computational cost of a QR factorization is $O(nd^2)$ operations.
Classical algorithms for computing the QR factorization, such as the LAPACK methods underlying [`np.linalg.qr`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.qr.html), are typically based on Householder reflections or Givens rotations.
These algorithms are numerically stable, but inherently sequential, leading to relatively low flop-rates on modern hardware.







