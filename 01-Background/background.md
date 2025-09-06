---
title: Introduction
description: Foundational computing principles for randomized numerical linear algebra including numerical linear algebra review and computational cost analysis.
keywords: [numerical linear algebra, background, computing principles, matrix computations, computational cost]
numbering:
  equation:
    enumerator: 1.%s
  proof:theorem:
    enumerator: 1.%s
  proof:algorithm:
    enumerator: 1.%s
  proof:definition:
    enumerator: 1.%s
  proof:proposition:
    enumerator: 1.%s
---

What is randomized numerical linear algebra? 

- **randomness** is the concession that we can't reliably predict how dice are going to land,[^rand] and
- **numerical linear algebra** is about algorithms for doing linear algebra on computers. 

[^rand]: "but dice are deterministic blah blah blah"

So, RandNLA is basically about understanding how we use the outcomes of unpredictable dice to do linear algebra on computers better (🎲+🖥️=🎉).


To some, it may seem unintuitive, or even disconcerting, that randomness, which we often associate with unpredicibility or unreliability, will be used as a tool in our algorithms.
We try to provide a brief justification the [role of randomness](./role-of-randomness.md) later in this chapter, ultimately, we take the pragmatic position that a philosophical justification of the use of randomness is mostly irrelevant.
Indeed, there are many examples of RandNLA algorithms that, in theory and in practice,  work better than their deterministic counterparts (with respect to essentially any reasonable metric).


This book is geared towards practical algorithms. 
However, to understand real-world algorithms, we need some understanding of how the computers we run them on work.
Unfortunately, how computers work is very mysterious. 
Later in this chapter, we explore some commons ways to think about the [cost of algorithms](./cost-of-numerical-linear-algebra.ipynb), which at least gives us a handle to thinking about 

:::{aside} How do computers work?
![](./rock.png)
:::


Basic background is on [NLA](./review-NLA.md) and [probability](./review-probability.md) is provided in the next section.
However, the book is written assuming readers are already familiar (at an undergrad level) with these topics.


