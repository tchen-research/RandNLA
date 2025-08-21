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

## The role of randomness

The output of a randomized algorithm is random 🧐. 
As such, the outputs of the same randomized algorithm run on the same input twice may differ.[^deterministic]


This has lead to some hesitance towards the use of randomized algorithms.


[^deterministic]: modern computers (which make use of parallelism) are also non-deterministic due to [race-conditions](https://en.wikipedia.org/wiki/Race_condition).


In RandNLA, the role of randomness is often to avoid pathological cases.
The [power method](https://en.wikipedia.org/wiki/Power_iteration) for computing the top eigenvalue of a positive definite matrix is a quintessential example of the role randomness tends to play in RandNLA.
By choosing the starting vector randomly, we can ensure that it has nonzero inner product with the top eigenvector of the input matrix, and hence that the algorithm converges to the top eigenvalue.
The accuracy and reliability of the algorithm are high, despite the fact that the algorithm is randomized.[^power-method]

[^power-method]: In fact, it is currently unknown how to efficiently compute the top eigenvalue of a positive definite matrix without randomization.



## Bounds

The measures of accuracy we use to measure random variables must take into account the fact that the output of randomized algorithms is a random variable. 
The two most common ways to do this are by expectation bounds or probability bounds. 


### Expectation bounds 

Expectation bounds measure the average error of the algorithm over repeated independent runs.
For instance, if $\vec{x}^*$ is the true solution to a problem and $\widehat{\vec{x}}$ is the output of a randomized algorithm, then we might hope to prove that
```{math}
:label: eqn-expectation-bound
\EE\left[\| \vec{x}^* - \widehat{\vec{x}} \|^2\right]
\leq \varepsilon^2.
```
Since the expectation has many nice properties (e.g. [linearity](https://en.wikipedia.org/wiki/Expected_value#Properties), [law of total expectation](https://en.wikipedia.org/wiki/Law_of_total_expectation), etc.) many algorithms admit simpler analyses when using expectation bounds.

### Probability bounds

Alternatively, we can use a *tail bound* to guarantee that the error is small with high probability.
These bounds take the form:
\begin{equation*}
\PP\left[\| \vec{x}^* - \widehat{\vec{x}} \| \leq \varepsilon\right]
\geq 1- \delta.
\end{equation*}
One major advantage of working with probability bounds is the ability to handle dependencies between the random variables by using a [union bound](https://en.wikipedia.org/wiki/Boole%27s_inequality): if two bad events are each unlikely to occur, then the probability that one or both bad events occurs is small, regardless of any correlation between the two events. 

### Boosting 

From a TCS perspective, in many settings, there is relatively little value in deriving tail bounds. 
In particular, by [Markov's inequality](https://en.wikipedia.org/wiki/Markov%27s_inequality), an expectation bound {eq}`eqn-expectation-bound` implies a tail bound of the form:
\begin{equation*}
\PP\left[\| \vec{x}^* - \widehat{\vec{x}} \| \leq 10 \varepsilon\right]
\geq \frac{99}{100}.
\end{equation*}
While the constant failure probability is not suitable for many applications, it can be improved by *boosting* the tail bound.
In particular, if we repeat the randomized algorithm $\log(1/\delta)$ times, then we guarantee that at least half of the runs have error at most $10\varepsilon$ with probability at least $1-\delta$.
Then there is a black-box post-processing step (which can be viewed as a generalization of the median) that allows an accurate output to be determined, so long as at least $2/3$ of the runs have error at most $10\varepsilon$.

### Which bound to use?


The choice between expectation and probability bounds depends on the application context. Expectation bounds are often easier to analyze and sufficient for theoretical understanding, especially when combined with boosting techniques.
However, probability bounds are generally preferred in practice because they provide stronger guarantees about individual algorithm runs and allow for more precise control over failure probability. For applications requiring reliability guarantees, probability bounds are essential.

