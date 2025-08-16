# Trace Estimation


A number of applications involve computing the trace of a matrix 
```{math}
\tr(\vec{A}) = \sum_{i=1}^n A_{ii}.
```
At first glance, it might seem silly that this book would spend any time on algorithms for this task. 
After all, we can compute the trace of a matrix by simply reading and summing its diagonal entries.
The challenge arises when $\vec{A}$ is not available explicitly, but is instead accessibly only as a block-box linear operator which we can access through [matrix-vector products](../Background/cost-of-numerical-linear-algebra.ipynb) $\vec{x} \mapsto \vec{A}\vec{x}$.




TODO: examples
