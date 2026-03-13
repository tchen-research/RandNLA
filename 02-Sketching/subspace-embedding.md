---
title: Subspace Embedding
description: Definition and characterization of subspace embeddings for preserving geometry in sketching methods
keywords: [subspace embedding, sketching, distortion, geometry preservation, singular values, orthonormal basis]
numbering:
  equation:
    enumerator: 2.%s
    continue: true
  proof:theorem:
    enumerator: 2.%s
    continue: true
  proof:algorithm:
    enumerator: 2.%s
    continue: true
  proof:definition:
    enumerator: 2.%s
    continue: true
  proof:proposition:
    enumerator: 2.%s
    continue: true
---

An important property of a sketching matrix is that it preserves the geometry of a subspace.
This is quantified by the following definition: 

:::{prf:definition} Subspace Embedding
:label: def-subspace-embedding

Let $V$ be a subspace of $\R^n$. We say a matrix $\vec{S}$ is a subspace embedding for $V$ with distortion parameters $(\alpha, \beta)$ where $0 < \alpha \leq 1 \leq \beta$ if
\begin{equation*}
\forall \vec{x}\in V: \alpha\|\vec{x}\| \leq \|\vec{S}\vec{x}\| \leq \beta\|\vec{x}\|.
\end{equation*}
When $V = \range(\vec{A})$ for some matrix $\vec{A}$, we say that $\vec{S}$ is a subspace embedding for $\vec{A}$.
:::

In particular, a subspace embedding ensures that the lengths of all vectors within a subspace are approximately preserved by the sketch. 

We note that it is common to use the parameterization
\begin{equation*}
\alpha = 1-\varepsilon
,\qquad
\beta = 1+\varepsilon.
\end{equation*}
In this case, it is common to say that $\vec{S}$ is an $\varepsilon$-subspace embedding.


## Equivalent Characterizations

It will sometimes be useful to work with the following equivalent characterizations of subspace embeddings:

:::{prf:theorem}
:label: thm-se-equivalent
Let $\vec{V}$ be an orthonormal basis for a subspace $V$ of $\R^n$. 
The following are equivalent:
- $\vec{S}$ is a subspace embedding for $V$ with distortion parameters $\alpha, \beta$
- $\forall \vec{c}\in \R^d: \alpha\|\vec{V}\vec{c}\| \leq \|\vec{S}\vec{V}\vec{c}\| \leq \beta\|\vec{V}\vec{c}\|$
- $\forall \vec{c}\in \R^d: \alpha\|\vec{c}\| \leq \|\vec{S}\vec{V}\vec{c}\| \leq \beta\|\vec{c}\|$
- $\| \vec{V}^\T \vec{S}^\T \vec{S} \vec{V} - \vec{I} \|_2 \leq \max\{\beta^2 - 1, 1 - \alpha^2\}$
- $\alpha \leq \smin(\vec{S}\vec{V}) \leq \smax(\vec{S}\vec{V}) \leq \beta$
:::

:::{prf:proof}
:class: dropdown
:enumerated: false
Suppose $\vec{S}$ is a subspace embedding for $V$.
Any $\vec{x} \in V$ can be written as $\vec{x} = \vec{V}\vec{c}$ for some $\vec{c} \in \R^d$.
Thus, the subspace embedding condition can be rewritten as (this is true even if $\vec{V}$ isn't orthonormal)
\begin{equation*}
\forall \vec{c}\in \R^d: \alpha\|\vec{V}\vec{c}\| \leq \|\vec{S}\vec{V}\vec{c}\| \leq \beta\|\vec{V}\vec{c}\|.
\end{equation*}
Since $\vec{V}$ is orthonormal, $\|\vec{V}\vec{c}\| = \|\vec{c}\|$ and hence we have the equivalent condition
\begin{equation*}
\forall \vec{c}\in \R^d: \alpha\|\vec{c}\| \leq \|\vec{S}\vec{V}\vec{c}\| \leq \beta\|\vec{c}\|.
\end{equation*}
We can rewrite this as 
\begin{equation*}
\smax(\vec{S}\vec{V}) = \max_{\vec{c}\in \R^d} \frac{\|\vec{S}\vec{V}\vec{c}\|}{\|\vec{c}\|} \leq \beta
,\qquad
\smin(\vec{S}\vec{V}) = \min_{\vec{c}\in \R^d} \frac{\|\vec{S}\vec{V}\vec{c}\|}{\|\vec{c}\|} \geq \alpha.
\end{equation*}
Finally, note that 
\begin{equation*}
\begin{aligned}
\| \vec{V}^\T \vec{S}^\T \vec{S} \vec{V} - \vec{I} \|_2
&= \max_{i} |\lambda_i(\vec{V}^\T \vec{S}^\T \vec{S} \vec{V}) - 1||
\\&= \max_{i} |\smax(\vec{S}\vec{V})^2 - 1|
\\&\leq \max\{ \beta^2 - 1, 1 - \alpha^2 \}.
\end{aligned}
\end{equation*}
:::


In TCS, where the rates as $\varepsilon\to0$ ($\alpha=1-\varepsilon$, $\beta=1+\varepsilon$) are important.
In this case, the set of "equivalent" definitions is larger.
For instance, the condition on the spectral norm simplifies to $\| \vec{V}^\T \vec{S}^\T \vec{S} \vec{V} - \vec{I} \|_2 \leq \varepsilon(2+\varepsilon)$, which is often written as $\| \vec{V}^\T \vec{S}^\T \vec{S} \vec{V} - \vec{I} \|_2 \leq \varepsilon$.
Similarly, in some cases, a subspace embedding is defined with respect to the squared norms, since $\sqrt{1+\varepsilon} = 1 + \varepsilon/2 + O(\varepsilon^2)$ as $\varepsilon \to 0$.
