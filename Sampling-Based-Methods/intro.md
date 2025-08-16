# Sampling-Based Methods

Sampling-based methods represent a different paradigm in randomized numerical linear algebra, where instead of using random projections or embeddings, we strategically sample rows, columns, or entries of matrices. These methods are particularly effective for sparse matrices and problems where communication costs dominate computation.

The key insight is that many matrix operations can be approximated by working with carefully chosen subsets of the data. The challenge lies in developing sampling strategies that preserve the essential spectral properties while dramatically reducing computational and storage requirements.

## Core Principles

Sampling-based approaches typically involve:
1. **Importance sampling**: Selecting rows/columns with probabilities proportional to their norms or leverage scores
2. **Uniform sampling**: Simple random sampling with appropriate rescaling
3. **Adaptive sampling**: Dynamic selection based on iterative refinement

This section covers:
- **Approximate Matrix Multiplication**: Fast algorithms for computing $AB^T$ approximately
- **Low-Rank Approximation**: CUR and related decompositions using sampled rows and columns
- **Cholesky**: Randomized pivoting strategies for Cholesky decomposition
- **CUR**: Column-Row factorizations that preserve interpretability
- **Active Regression**: Adaptive sampling for regression problems
- **SGD/Kaczmarz**: Stochastic gradient methods and their randomized variants

These methods are particularly valuable in distributed computing environments and for very large sparse matrices where traditional dense methods are prohibitive.