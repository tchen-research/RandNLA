# Randomized Numerical Linear Algebra

Randomized Numerical Linear Algebra (RandNLA) is a subfield of [numerical linear algebra](https://en.wikipedia.org/wiki/Numerical_linear_algebra) that focuses on the use of randomization as a tool to develop more efficient/accurate algorithms for solving linear algebra tasks.
Many RandNLA algorithms are remarkably simple, while providing significant speedups over traditional methods.

This book aims to provide a *practical introduction* to the fundamental concepts and techniques in RandNLA through simple mathematical explanations and accompanying code examples.
We focus on intuition, conceptual understanding, and ~vibes~.
More mathematically detailed treatments are left to existing literature.

This is a living document, and we welcome contributions and suggestions for improvement.
In particular readers can fix typos, update or add references/experiments/information, and suggest changes on Github.




## Prerequisites

Readers are expected to be familiar with (numerical) linear algebra.
We assume readers have a basic understanding of [matrix factorizations](https://en.wikipedia.org/wiki/Matrix_decomposition) (e.g. QR, SVD, etc.) and concepts like [stability](https://en.wikipedia.org/wiki/Numerical_stability) and [conditioning](https://en.wikipedia.org/wiki/Condition_number).
A basic overview is provided [here](../Background/review.ipynb).


## Other Resources


There are many existing resources on RandNLA.

- {cite:p}`martinsson_tropp_20`: General overview
- {cite:p}`murray_etal_23`: Implementation focused
- {cite:p}`tropp_webber_23`: Low-rank approximation

TODO

## References
```{bibliography}
:filter: docname in docnames
```