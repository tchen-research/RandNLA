# Girard-Hutchinson Estimator

Let $\vec{x}$ be a random vector satisfying $\mathbb{E}[\vec{x}] = \vec{0}$ and $\mathbb{E}[\vec{x}\vec{x}^\T] = \vec{I}$.
Then, a direct computations reveals that $\vec{x}^\T\vec{A}\vec{x}$ is an unbiased estimator of the trace of $\vec{A}$. 
In particular, by the cylic property of the trace and linearity of expectation,
\begin{equation*}
\EE[ \vec{x}^\T \vec{A}\vec{x}] 
= \EE[ \tr(\vec{x}^\T \vec{A}\vec{x}) ] 
= \EE[ \tr(\vec{A}\vec{x}\vec{x}^\T ) ] 
= \tr(\vec{A}\EE[ \vec{x}\vec{x}^\T ] )
= \text{tr}(\vec{A}).
\end{equation*}
This suggests a simple randomized estimator.
:::{prf:definition} Girard-Hutchinson Estimator
:label: def:girard_hutchinson_estimator
Fix an integer $m \geq 1$. The *Girard-Hutchinson trace estimator* is
\begin{equation*}
\widehat{\tr}_m(\vec{A}) := \frac{1}{m}\sum_{i=1}^{m} \vec{x}_i^\T \vec{A} \vec{x}_i,
\end{equation*}
where $\vec{x}_i$ are iid copies of some vector $\vec{x}$ satisfying $\mathbb{E}[\vec{x}] = \vec{0}$ and $\mathbb{E}[\vec{x}\vec{x}^\T] = \vec{I}$.
:::
```{aside} History
This estimator is often referred to as *Hutchinson's trace estimator*, especially when $\vec{x}$ is a random Rademacher vector.
However, {cite:p}`hutchinson_89` itself cites {cite:p}`girard_87` which addresses the same task by using samples of $\vec{x}$ drawn uniformly from the unit hypersphere.
See {cite:p}`chen_22` for more discussion.
```

A standard computation reveals that 
\begin{equation*}
\EE[ \widehat{\tr}_m(\vec{A}) ] = \tr(\vec{A}),
\qquad
\VV[ \widehat{\tr}_m(\vec{A}) ] = \frac{1}{m} \VV[\vec{x}^\T\vec{A}\vec{x}].
\end{equation*}
Thus, by increasing $m$, we can reduce the variance of the estimator to be arbitrarily small. 

Three common choices of $\vec{x}$ are Gaussian, random unit vectors, and Rademacher random variables:
- **Gaussian:** Each component of $\vec{x}$ is iid $\mathcal{N}(0,1)$.
- **Random unit vector (real):** Each component of $\vec{x}$ is iid $\mathcal{N}(0,1)$, and then $\vec{x}$ is normalized to have norm $\sqrt{n}$.
- **Rademacher:** Each component of $\vec{x}$ is iid $\{-1,1\}$ with equal probability. 

When $\vec{A}$ is symmetric, the variance of the estimator can be computed explicitly:
| Distribution of $\vec{x}$ | Variance:  $\VV[\vec{x}^\T\vec{A}\vec{x}]$ |
|-------|-----|
| Gaussian     | $2 \Vert\vec{A}\Vert_\F^2$ |
|  Rademacher  | $2 (\Vert\vec{A}\Vert_\F^2 - \sum_i A_{ii}^2)$ |
| Uniform (real)     | $\frac{2n}{n+2} \left( \Vert \vec{A} \Vert_\F^2 - \frac{1}{n}\tr(\vec{A})^2 \right)$ |

If $\vec{A}$ is not symmetric, we can use the fact that $\widehat{\tr}_m(\vec{A})=\widehat{\tr}_m((\vec{A} + \vec{A}^\T)/2)$.
Readers can refer to Ethan's [blog post](https://www.ethanepperly.com/index.php/2023/01/26/stochastic-trace-estimation/) for a derivation of the variances listed above, as well as some additional discussion on interesting optimality properties of certain distributions.




```{bibliography}
:filter: docname in docnames
```