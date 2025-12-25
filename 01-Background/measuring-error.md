---
title: Measuring error
description: Methods for quantifying accuracy in randomized numerical linear algebra algorithms including a priori bounds, expectation bounds, probability bounds, and practical stopping criteria
keywords: [error analysis, expectation bounds, probability bounds, tail bounds, accuracy, a priori bounds, a posteriori bounds, stopping criteria, boosting, median trick]
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


Understanding the accuracy of RandNLA algorithms is critical to their effective use.
Of course, as with measuring the [cost of numerical algorithms](./cost-of-numerical-linear-algebra.ipynb), there are many different ways to quantify the accuracy of RandNLA algorithms.


## A priori bounds

Much of the theory for RandNLA focuses on worst-case prior bounds.
That is, bounds that gives accuracy guarantees for an algorithm (with the right choice of parameters) on every problem in a problem class, prior to running the algorithm.
This is similar to guarantees for deterministic algorithms. 
However, the measures of accuracy we use must take into account the fact that the output of a randomized algorithm is random 🧐, and may therefore change from run to run.
The two most common ways to do this are by expectation bounds or probability bounds. 

### Expectation bounds 

Expectation bounds measure the average error of the algorithm over repeated independent runs.
For instance, if $\vec{x}^*$ is the true solution to a problem and $\widehat{\vec{x}}$ is the output of a randomized algorithm, then we might hope to prove that
```{math}
:label: eqn-expectation-bound
\EE\left[\| \vec{x}^* - \widehat{\vec{x}} \|^2\right]
\leq \varepsilon^2.
```
Analyses of an algorithm will aim to parameterize the costs of the algorithm in terms of the accuracy $\varepsilon$.


Since the expectation has many nice properties (e.g. [linearity](https://en.wikipedia.org/wiki/Expected_value#Properties), [law of total expectation](https://en.wikipedia.org/wiki/Law_of_total_expectation), etc.) many algorithms admit simpler analyses when using expectation bounds.

### Probability bounds

Probability bounds (also called tail bounds) guarantee that the error of a given run of the algorithm is small with high probability.
These bounds take the form:
```{math}
\PP\left[\| \vec{x}^* - \widehat{\vec{x}} \| \leq \varepsilon\right]
\geq 1- \delta.
```
Analyses of an algorithm will aim to parameterize the costs of the algorithm in terms of the accuracy $\varepsilon$ and the failure probability $\delta$.

One major advantage of working with probability bounds is the ability to handle dependencies between the random variables by using a [union bound](https://en.wikipedia.org/wiki/Boole%27s_inequality): if two bad events are each unlikely to occur, then the probability that one or both bad events occurs is small, regardless of any correlation between the two events. 


### Expectation or probability?

The choice between expectation and probability bounds depends on the application context. 
Probability bounds are perhaps more intuitive to the general user, particularly in the case where the failure probability $\delta$ is so small as to never occur in practice.
However, by [Markov's inequality](#def-markov), an expectation bound {eq}`eqn-expectation-bound` implies a tail bound of the form:
\begin{equation*}
\PP\left[\| \vec{x}^* - \widehat{\vec{x}} \| \leq 10 \varepsilon\right]
\geq \frac{99}{100}.
\end{equation*}
On the other hand, a probability bound does not necessarily say anything about how bad the algorithm is in the bad cases, so an expectation bound cannot always be derived from a probability bound.
In addition, it is sometimes much easier to analyze an algorithm using one type of bound than the other.


#### Boosting / median-trick

If we are interested in the existence of an algorithm for a task (this is often the case in TCS) as opposed to the analysis of a particular algorithm, then it is unimportant to quantify the dependence of the cost on the failure probability. 
The reason is that any algorithm that succeeds with some constant probability $\delta_0>1/2$ can be converted to an algorithm that succeeds with arbitrary probability $\delta$ with only logarithmic overhead. 
In particular, by independently running the algorithm $O(\log(1/\delta))$ times, we can guarantee that, with probability at least $1-\delta$, more than half of the runs of the algorithm succeed.
There is then a black-box procedure for identifying a point near of the successful runs (in 1 dimension, you can just take the median).



## A posteriori bounds / practical stopping criteria

Prior bounds are typically parameterized in terms of unknown properties of the problem instance (e.g. the singular values of an input matrix), and the constants in the bounds may be pessimistic or even unknown. 
This immediately limits the practical use of such bounds.
Moreover, the behavior of an algorithm on a *particular input instance* is often much better than predicted by worst-case bounds.[^instance]

[^instance]: While there are some cases of instance-specific a priori bounds (e.g. instance-optimality for Krylov methods), these bounds are almost always are parameterized in terms of unknown properties of the problem instance. 

In total, this means that a practical algorithm requires some way of choosing parameters, such as the stopping criteria.
Fortunately, in many cases, there are ways to compute or estimate the error of an NLA algorithm. 
For example, the residual can be used to measure the accuracy of an approximate solution to a linear system of equations.

Interestingly, in many cases, the use of randomness in a RandNLA algorithm can actually *help* quantify the error. 
For example, we can use techniques like bootstrapping to estimate the variance of certain RandNLA algorithms with little computational overhead {cite:p}`epperly_tropp_24`.


## Some more thoughts

Prior bounds are useful for establishing upper bounds on the theoretical complexity of a linear algebra *task*.
They are also useful in establishing rates of convergence of an algorithm and understanding the dependence of an algorithm on certain properties of a problem, both of which can help inform the user about the suitability of a given algorithm for a given problem.[^upper-to-upper]
However, there seems to be a bit of an obsession in proving marginally better prior bounds for a given algorithm just for the sake of proving something.

[^upper-to-upper]: You can't compare upper bounds of one algorithm to upper bounds of another algorithm and conclude that one is better than the other! You need some sort of lower bounds (e.g. by knowing that the upper bound is pretty sharp in practice).

On the other hand, despite being arguably more important for practical computations, a posteriori bounds and parameter section techniques seem to be far less emphasized by the NLA community.




