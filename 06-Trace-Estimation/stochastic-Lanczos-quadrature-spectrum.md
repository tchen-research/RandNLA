---
title: Stochastic Lanczos Quadrature
description: Combining Lanczos method with Girard-Hutchinson estimator for matrix function trace estimation
keywords: [stochastic Lanczos quadrature, SLQ, Lanczos method, quadratic forms, matrix functions, polynomial approximation, error bounds]
numbering:
  equation:
    enumerator: 6.%s
    continue: true
  proof:theorem:
    enumerator: 6.%s
    continue: true
  proof:algorithm:
    enumerator: 6.%s
    continue: true
  proof:definition:
    enumerator: 6.%s
    continue: true
  proof:proposition:
    enumerator: 6.%s
    continue: true
---

In the previous section, we introduced SLQ as a combination of the Girard-Hutchinson trace estimator and a black-box Lanczos-based method for approximating quadratic forms.
To truly understand the algorithm, particularly its behavior in finite precision arithmetic, it is informative to view SLQ and related algorithms through their relation to [quadrature](https://en.wikipedia.org/wiki/Quadrature_(mathematics)).
This perspective is taken in {cite:p}`chen_24`.
We provide a brief summary here.


## Connection to quadrature

Fix a vector $\vec{x}$ and consider the weighted spectral density 
```{math}
\psi(x;\vec{A},\vec{x}) := \frac{1}{n} \sum_{i=1}^{n} |\vec{x}^\T \vec{u}_i|^2 \delta(x-\lambda_i).
```
and observe that 
```{math}
\vec{x}^\T f(\vec{A})\vec{x} = n \int_{-\infty}^{\infty} f(x) \psi(x;\vec{A},\vec{x}) \d{x}.
```
Note that when $\vec{x}$ is drawn from a suitable distribution ($\EE[\vec{x}\vec{x}^\T] = \vec{I}$), then $\EE[\psi(x)] = \varphi(x)$.


Let $\vec{T}$ be the output of the Lanczos algorithm run on $(\vec{A},\vec{x})$ for $k$ iterations, and suppose $\vec{T}$ has eigendecomposition $\vec{T} = \sum_{j=1}^{k} \vec{\theta}_{j} \vec{s}_{j} \vec{s}_{j}^\T$.
Define weights $\omega_{j} = \| \vec{x}\|^2 | \vec{e}_1^\T \vec{s}_{j}|^2$.
Consider the probability density 
```{math}
\psi_k(x;\vec{A},\vec{x}) := \frac{1}{n} \sum_{j=1}^{k} \omega_{j} \delta(x-\theta_{j}).
```
This is the [Gaussian quadrature](https://mathworld.wolfram.com/GaussianQuadrature.html) approximation to $\psi(x)$; i.e. the unique density function supported on $k$ points whose moments match $\psi(x)$ through degree $2k-1$. 




## Randomized matrix-free quadrature

Hence, the [SLQ approximation](#def-slq-spec) is nothing more than the average of the Gaussian quadrature approximations to weighted spectral densities corresponding to random vectors $\vec{x}_i$.


:::{prf:definition} Stochastic Lanczos Quadrature
:label: def-slq-spec

The *stochastic Lanczos quadrature* approximation to $\phi(x;\vec{A})$ is 
\begin{equation*}
\varphi_{k,m}^{\Call{SLQ}}(x;\vec{A})
= \frac{1}{m} \sum_{i=1}^{m} \psi_k(x;\vec{A},\vec{x}_i).
\end{equation*}
:::


Observe that the SLQ spectrum approximation defined here, and the [SLQ trace estimator](#slq-trace) are compatible:
```{math}
:label: slq-equivalence

\Call{SLQ}_{k,m}(f;\vec{A}) = n \int f(x) \varphi_{k,m}^{\Call{SLQ}}(x;\vec{A}) \d{x}.
```

As in the case of spectral sum approximation, increasing $k$ and $m$ increases the quality of the approximation. 
For instance, we have the following:

:::{prf:theorem}


Suppose the $\vec{x}_i$ are independent normalized Gaussian vectors (uniform from the sphere of radius $\sqrt{n}$).
Then for some
\begin{equation*}
 m = \tilde{O}\left( \frac{1}{n \varepsilon^2} \right)
 ,\quad 
 k = O\left( \frac{1}{\varepsilon} \right),
\end{equation*}
with probability at least $1-\delta$,
\begin{equation*}
\operatorname{W}(\varphi(\cdot;\vec{A}),\varphi_{k,m}^{\Call{SLQ}}(\cdot;\vec{A}))
\leq \varepsilon | \smax(\vec{A}) - \smin(\vec{A})|.
\end{equation*}
:::

:::{prf:proof}
:class: dropdown 
:enumerated: false

Full proofs can be found in {cite:p}`chen_trogdon_ubaru_21,chen_24,chen_trogdon_ubaru_25`, but the basic idea is relatively straightforward. 


First, one notes that the Wasserstein distance has an equivalent definition 
\begin{equation*}
\operatorname{W}(\varphi_1,\varphi_2) = \sup_{f\text{ 1-Lipshitz}} \int_{-\infty}^{\infty} f(x) (\varphi_1(x) - \varphi_2(x)) \d{x}.
\end{equation*}

For a *fixed* 1-Lipshitz functions, {prf:ref}`slq-equivalence` and {prf:ref}`slq-func` give that $m = O(1/(n\varepsilon^2))$ and $m = O(1/\varepsilon)$ (since the best $2k-1$ polynomial approximation to 1-Lipshitz functions converges like $\sim 1/k$).

However, to bound the Wasserstein distance, we require the result holds for *all* 1-Lipshitz functions. 
They key to extending to all 1-Lipshitz functions is to observe that Lipshitz functions have a stable Chebyshev series; i.e. a slight perturbation to their Chebyshev approximation still yields a good approximation. 
Therefore, if we can approximate the Chebyshev moments of $\varphi(x;\vec{A}) (traces of the Chebyshev polynomials) well, then we can (up to a slight loss) approximate any Lipshitz function.
:::

