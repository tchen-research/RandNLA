# Low-Rank Approximation

Low-rank approximation is a fundamental problem in numerical linear algebra with applications spanning data compression, machine learning, and scientific computing. Given a matrix $A \in \mathbb{R}^{m \times n}$, the goal is to find a matrix $\tilde{A}$ of rank $k \ll \min(m,n)$ that minimizes $\|A - \tilde{A}\|$ in some appropriate norm.

The classical approach involves computing the full singular value decomposition (SVD), which requires $O(\min(m,n)^3)$ operations. However, when only a low-rank approximation is needed, randomized methods can dramatically reduce this computational cost while maintaining high accuracy.

This section covers:
- **Randomized SVD**: The foundational randomized algorithm for low-rank approximation
- **Subspace Iteration and Block Krylov**: Advanced techniques for improved accuracy and robustness
- **Nyström and Generalized Nyström**: Methods for symmetric and positive semidefinite matrices

These randomized approaches typically require only $O(mnk)$ operations and are particularly effective when $k$ is small relative to the matrix dimensions.