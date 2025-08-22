---
title: The role of randomness
description: Understanding the role of randomness in randomized numerical linear algebra algorithms, including expectation bounds, probability bounds, and boosting techniques
keywords: [randomness, probability bounds, expectation bounds, boosting, tail bounds, Markov inequality, randomized algorithms]
numbering:
  equation:
    enumerator: 1.%s
    continue: true
  proof:theorem:
    enumerator: 1.%s
    continue: true
  proof:algorithm:
    enumerator: 1.%s
    continue: true
  proof:definition:
    enumerator: 1.%s
    continue: true
  proof:proposition:
    enumerator: 1.%s
    continue: true
---

Loosely speaking, a randomized algorithm is an algorithm that's allowed to flip coins to make decisions during its execution.[^randalg]
Clearly a randomized algorithm can do anything a deterministic algorithm can do, since it can simply ignore the random bits it generates.
Thus, the question is, what can randomized algorithms do that deterministic algorithms cannot?

[^randalg]: Theoretically speaking, randomized algorithms are deterministic algorithms which take as input the problem and a list of random bits.
[^deterministic]: modern computers (which make use of parallelism) are also non-deterministic due to [race-conditions](https://en.wikipedia.org/wiki/Race_condition).


## Solving otherwise intractable problems

The first way randomness helps is by allowing us to solve problems that would otherwise be impossible! 

Suppose we are given an unsorted list of $n$ numbers, and are tasked with finding a number that's in the top 10\% of the largest numbers in the list.
Any deterministic algorithm for this problem must inspect every number in the list.
However, it's not hard to see that a randomized algorithm can solve this problem with very high probability by simply uniformly sampling a few numbers from the list and returning the largest number among those sampled.
Indeed, any given sample has a 10\% chance of being in the top 10\%, so if we take a few dozen samples, the probability that none of them are in the top 10\% is vanishingly small.

Numerical algorithms can benefit from randomization in a similar way. 
For example, a number of problems can be solved by looking at only a random subset of the data or by compressing a stream of the data on the fly.
In such settings, randomization allows us to get some approximate answer, when it would otherwise be impossible to get any answer at all.
Thus, even if the randomized algorithm is not particularly accurate, it may be the only option available.


## Randomness as a preconditioner

Many RandNLA algorithms use randomness in a much milder way: as a means to avoid pathological cases.

The [power method](https://en.wikipedia.org/wiki/Power_iteration) for computing the top eigenvalue of a positive definite matrix is a nice example of the role randomness tends to play in RandNLA.
By choosing the starting vector randomly, we can ensure that it has nonzero inner product with the top eigenvector of the input matrix, and hence that the algorithm converges to the top eigenvalue.
The accuracy and reliability of the algorithm are high, despite the fact that the algorithm is randomized.[^power-method]

[^power-method]: In fact, it is currently unknown how to efficiently compute the top eigenvalue of a positive definite matrix without randomization.

Another key example is the use of randomness to construct a [preconditioner](https://en.wikipedia.org/wiki/Preconditioner) for regression problems. 
Here it is possible to obtain extremely good preconditioners that guarantee rapid convergence of iterative methods.
Again, the accuracy and reliability of the algorithm are high, since all that we need to guarantee is that the preconditioned problem is reasonably well-conditioned.




