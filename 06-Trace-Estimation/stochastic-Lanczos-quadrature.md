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
:::{aside} Why "quadrature"?
The Lanczos method for quadratic forms can be viewed as a Gaussian quadrature approximation to a certain integral. 
This connection and the full details of the algorithm are explained in detail in {cite:p}`chen_24,chen_trogdon_ubaru_25`.
:::
Recall that using $k-1$ matrix-vector products with $\vec{A}$, the [Lanczos method for quadratic forms](def:lanczos-method) produces an approximation $\Call{Lan-QF}_k(f;\vec{A},\vec{x})$ that is an approximation to $\vec{x}^\T f(\vec{A})\vec{x}$.
Stochastic Lanczos Quadrature (SLQ) simply combines this method with the [Girard-Hutchinson trace estimator](def:girard_hutchinson_estimator).


````{prf:definition} Stochastic Lanczos Quadrature
The *Stochastic Lanczos Quadrature* (SLQ) estimator for the spectral sum $\tr(f(\vec{A}))$ is given by
\begin{equation*}
\Call{SLQ}_{k,m}(f;\vec{A}) := \frac{1}{m} \sum_{i=1}^{m} \Call{Lan-QF}_k(f;\vec{A},\vec{x}_i),
\end{equation*}
where $\vec{x}_i$ are independent standard Gaussian vectors.
````

A simple application of the triangle inequality gives a bound on expected squared error of the SLQ estimator.

:::{prf:theorem} 

For any $k,m\geq 1$, the SLQ estimator uses $(k-1)m$ matrix-vector products to $\vec{A}$ and satisfies
\begin{equation*}
\EE\left[ | \tr(f(\vec{A})) - \Call{SLQ}_{k,m}(f;\vec{A}) |^2 \right]
\leq \frac{4\| f(\vec{A}) \|_\F^2}{m} + 6n^2  \min_{\deg(p)<2k-1} \left( \max_{x\in[\lambda_n,\lambda_1]} | f(x) - p(x) | \right).
\end{equation*}
:::


:::{prf:proof}
:class: dropdown 
:enumerated: false

By the triangle inequality and since $(x+y)^2\leq 2(x^2+y^2)$, we have
\begin{equation*}\begin{aligned}
\hspace{1em}&\hspace{-1em}| \tr(f(\vec{A})) - \Call{SLQ}_{k,m}(f;\vec{A}) |^2
\\&\leq 2\left| \tr(f(\vec{A})) - \frac{1}{m}\sum_{i=1}^{m} \vec{x}_i^\T f(\vec{A})\vec{x}_i \right|^2 + 2\left| \frac{1}{m}\sum_{i=1}^{m} \vec{x}_i^\T f(\vec{A})\vec{x}_i - \Call{Lan-QF}_k(f;\vec{A},\vec{x}_i) \right|^2.
\end{aligned}\end{equation*}

Note that 
\begin{equation*}
\EE\left[ \left| \tr(f(\vec{A})) - \frac{1}{m}\sum_{i=1}^{m} \vec{x}_i^\T f(\vec{A})\vec{x}_i \right|^2 \right]
= 
\VV\left[ \widehat{\tr}_m(f(\vec{A})) \right]
= \frac{2 \| f(\vec{A}) \|_\F^2}{m},
\end{equation*}
where $\widehat{\tr}_m(\cdot)$ is the [Girard--Hutchinson estimator](./girard-hutchinson.ipynb#def:girard_hutchinson_estimator).

Next, by the triangle inequality and {prf:ref}`thm:lanczos_FA_polynomial`, 
\begin{equation*}\begin{aligned}
\hspace{2em}&\hspace{-2em}
\left| \frac{1}{m}\sum_{i=1}^{m} \vec{x}_i^\T f(\vec{A})\vec{x}_i - \Call{Lan-QF}_k(f;\vec{A},\vec{x}_i) \right|
\\&\leq \frac{1}{m}\sum_{i=1}^{m} \left| \vec{x}_i^\T f(\vec{A})\vec{x}_i - \Call{Lan-QF}_k(f;\vec{A},\vec{x}_i) \right|
\\&\leq \frac{1}{m} \sum_{i=1}^{m} \|\vec{x}_i\|^2 \min_{\deg(p)<2k-1} \max_{x\in[\lambda_n,\lambda_1]} | f(x) - p(x) |.
\end{aligned}\end{equation*}
Hence, 
\begin{equation*}\begin{aligned}
\hspace{2em}&\hspace{-2em}
\EE\left[ \left| \frac{1}{m}\sum_{i=1}^{m} \vec{x}_i^\T f(\vec{A})\vec{x}_i - \Call{Lan-QF}_k(f;\vec{A},\vec{x}_i) \right|^2 \right]
\\&\leq \frac{1}{m^2}\EE\left[  \left(\sum_{i=1}^{m} \|\vec{x}_i\|^2 \right)^2 \right] \min_{\deg(p)<2k-1} \max_{x\in[\lambda_n,\lambda_1]} | f(x) - p(x) |
\end{aligned}\end{equation*}
Now, note that $\sum_{i=1}^{m} \|\vec{x}_i\|^2$ is a Chi-squared random variable with $mn$ degrees of freedom. 
By looking on [Wikipedia](https://en.wikipedia.org/wiki/Chi-squared_distribution), we see that
\begin{equation*}
\EE\left[  \left(\sum_{i=1}^{m} \|\vec{x}_i\|^2 \right)^2 \right] = 2mn + (mn)^2 \leq 3(mn)^2.
\end{equation*}
Combining all of the above gives the result.

:::

Note that for "nice" functions $f(x)$, the error of the best polynomial approximation decreases exponentially with $k$ {cite:p}`trefethen_19`.