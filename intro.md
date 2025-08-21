---
title: Randomized Numerical Linear Algebra with Examples
description: A practical introduction to randomized numerical linear algebra (RandNLA) covering fundamental concepts, techniques, and algorithms with theoretical analysis and numerical experiments.
keywords: [randomized algorithms, numerical linear algebra, RandNLA, matrix factorizations, sketching, randomization, linear algebra]
numbering: false
---

Randomized Numerical Linear Algebra (RandNLA) is a subfield of [numerical linear algebra](https://en.wikipedia.org/wiki/Numerical_linear_algebra) that focuses on the use of randomization as a tool to develop more efficient/accurate algorithms for solving linear algebra tasks.
Many RandNLA algorithms are remarkably simple, while providing significant speedups over traditional methods.

This book aims to provide a *practical introduction* to the fundamental concepts and techniques in RandNLA. 
We focus on intuition and conceptual understanding, and provide a mixture of theoretical analysis and  numerical experiments.
This book does not aim to be a comprehensive survey of state of the field, but rather a first introduction to the subject.

Readers are expected to be familiar with (numerical) linear algebra.
We assume readers have a basic understanding of [matrix factorizations](https://en.wikipedia.org/wiki/Matrix_decomposition) (e.g. QR, SVD, etc.) and concepts like [stability](https://en.wikipedia.org/wiki/Numerical_stability) and [conditioning](https://en.wikipedia.org/wiki/Condition_number).
A basic refresher is provided [here](../01-Background/review.ipynb).

## Contributing

This is a living document, and we welcome contributions and suggestions for improvement.
In particular readers can fix typos, update or add references/experiments/information, and suggest changes on Github.

## Other Resources


There are many existing resources on RandNLA. The following surveys are of particular note:

- {cite:p}`martinsson_tropp_20`: This survey describes many RandNLA algorithms that have a proven track record for real-world problem instances. The paper treats both the theoretical foundations of the subject and the practical computational issues. 

- {cite:p}`murray_etal_23`: This survey explores randomized numerical linear algebra from a software development perspective, emphasizing the potential for standardized "RandBLAS" and "RandLAPACK" libraries to make these algorithms more accessible to practitioners. 

- {cite:p}`tropp_webber_23`: This survey focuses specifically on randomized algorithms for computing low-rank matrix approximations. The work provides detailed non-asymptotic analyses of the performance of these algorithms and contains numerical examples to illustrate the effectiveness of the algorithms.

- {cite:p}`woodruff_14`: This is an early work on sketching, that provides a TCS-flavored overview of the field as of 2014. The focus is mostly on proving rates, and many of the key concepts in RandNLA are covered.

In addition, we highly recommend [Ethan Epperly's blog](https://www.ethanepperly.com/index.php/posts-by-topic/), which contains many accessible posts on RandNLA topics, as well as numerical experiments and code snippets.

```{bibliography}
:filter: docname in docnames
```


