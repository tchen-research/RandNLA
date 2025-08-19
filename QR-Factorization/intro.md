#  Exact Factorization

In this chapter we focus on algorithms for computing a QR factorization of a tall matrix $\vec{A}\in\R^{n\times d}$, where $n\gg d$.
The computational cost of a QR factorization is $O(nd^2)$ operations.
Classical algorithms for computing the QR factorization, such as the LAPACK methods underlying [`np.linalg.qr`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.qr.html), are typically based on Householder reflections or Givens rotations.
These algorithms are numerically stable, but inherently sequential, leading to relatively low flop-rates on modern hardware.


Many of the ideas we discuss in this chapter can be used to compute a singular value decomposition (SVD). 
Alternately, on obtain an SVD decomposition of $\vec{A}$ efficiently from a QR factorization.
Simply compute an SVD $\vec{R} = \vec{U}' \vec{\Sigma} \vec{V}^\T$ and then set $\vec{U} = \vec{Q} \vec{U}'$ to obtain an SVD
\begin{equation*}
\vec{A} = \vec{U} \vec{\Sigma} \vec{V}^\T.
\end{equation*}



