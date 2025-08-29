---
title: Trace Estimation
description: Randomized algorithms for estimating matrix traces when matrices are accessible only through matrix-vector products
keywords: [trace estimation, matrix-vector products, implicit matrices, black-box linear operators, differential equations, matrix functions]
numbering:
  equation:
    enumerator: 6.%s
  proof:theorem:
    enumerator: 6.%s
  proof:algorithm:
    enumerator: 6.%s
  proof:definition:
    enumerator: 6.%s
  proof:proposition:
    enumerator: 6.%s
  heading_2: false
---

At first glance, it might seem silly that this book would spend any time on algorithms for this task. 
After all, we can compute the trace of a matrix by simply reading and summing its diagonal entries.
The challenge arises when $\vec{A}$ is not available explicitly, but is instead accessibly only as a block-box linear operator which we can access through [matrix-vector product queries](../01-Background/cost-of-numerical-linear-algebra.ipynb#matrix-queries).

:::{prf:definition} Implicit Trace Estimation
:label: task-trace-est
Given $\vec{A}\in\R^{n\times n}$, estimate 
\begin{equation*}
\tr(\vec{A}) = \sum_{i=1}^n A_{ii}
\end{equation*}
using only matrix-vector products with $\vec{A}$.
:::

Some settings where $\vec{A}$ is most naturally accessed implicitly include:
- $\vec{A}$ is the solution operator to a differential equation, and $\vec{x} \mapsto \vec{A}\vec{x}$ is computed by a numerical solver.
- $\vec{A} = f(\vec{B})$, and $\vec{x} \mapsto f(\vec{B})\vec{x}$ can be computed using a black-box method for matrix functions such as Lanczos.
    - A special case is $\vec{A} = \vec{B}^{-1}$, where $\vec{x} \mapsto \vec{B}^{-1}\vec{x}$ is computed by solving a linear system using Conjugate Gradient or some other fast solver.


## Further Reading

- @girard_87, @hutchinson_89: First papers on stochastic trace estimation
- @epperly_23: Nice derivation of the variance of stochastic trace estimators.
- @chen_24: Book on Lanczos methods for matrix functions, which includes content on spectrum and spectral sum approximation. See references within for connection to physics.
