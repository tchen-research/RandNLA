# Trace Estimation


A number of applications involve computing the trace of a matrix 
```{math}
\tr(\vec{A}) = \sum_{i=1}^n A_{ii}.
```
At first glance, it might seem silly that this book would spend any time on algorithms for this task. 
After all, we can compute the trace of a matrix by simply reading and summing its diagonal entries.
The challenge arises when $\vec{A}$ is not available explicitly, but is instead accessibly only as a block-box linear operator which we can access through [matrix-vector products](../Background/cost-of-numerical-linear-algebra.ipynb) $\vec{x} \mapsto \vec{A}\vec{x}$.


For example, some settings where $\vec{A}$ is most naturally accessed implicitly include:
- $\vec{A}$ is the solution operator to a differential equation, and $\vec{x} \mapsto \vec{A}\vec{x}$ is computed by a numerical solver.
- $\vec{A} = f(\vec{B})$, and $\vec{x} \mapsto f(\vec{B})\vec{x}$ can be computed using a black-box method for matrix functions such as Lanczos.
    - A special case is $\vec{A} = \vec{B}^{-1}$, where $\vec{x} \mapsto \vec{B}^{-1}\vec{x}$ is computed by solving a linear system using Conjugate Gradient or some other fast solver.
