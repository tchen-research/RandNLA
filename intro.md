---
title: Randomized Numerical Linear Algebra with Examples
description: A practical introduction to randomized numerical linear algebra (RandNLA) covering fundamental concepts, techniques, and algorithms with theoretical analysis and numerical experiments.
keywords: [randomized algorithms, numerical linear algebra, RandNLA, matrix factorizations, sketching, randomization, linear algebra]
numbering: false
---

Randomized Numerical Linear Algebra (RandNLA) is a subfield of [numerical linear algebra](https://en.wikipedia.org/wiki/Numerical_linear_algebra) that focuses on the use of randomization as a tool to develop more efficient/accurate algorithms for solving linear algebra tasks.
Many RandNLA algorithms are remarkably simple, while providing significant speedups over traditional methods.

## This "book"

This book aims to provide a *practical introduction* to some of the fundamental concepts and techniques in RandNLA.
We focus on intuition and conceptual understanding, and provide a mixture of theoretical analysis and accompanying numerical experiments.
Jupyter notebooks with the code examples can be downloaded from [Github](https://github.com/tchen-research/RandNLA).

The intended audience is students and researchers new to the topic.
Readers are expected to be familiar with (numerical) linear algebra and probability, but a basic refresher is provided [here](../01-Background/review.md).
The content covered would be appropriate for a short module on RandNLA in a numerical linear algebra course, or even as a weekend read for PhD students with a strong background in numerical linear algebra.


The majority of the book is dedicated to a collection of RandNLA algorithms for core linear algebra tasks that can often serve as *drop in replacements* for classical linear algebra methods, while providing order-of-magnitude speedups 🤯.
We view these methods as conceptually important and practically useful, especially for practitioners.
These methods are characterized by the fact that their effectiveness is easily demonstrated in simple numerical experiments. 
For example, the [Randomized SVD](./05-Low-Rank-Approximation/randomized-svd.ipynb) can be implemented in just a few lines of code, and produces high-quality low-rank approximations way faster than the exact SVD.


We also provide an introduction to [sampling-based methods](./07-Sampling-Based-Methods/). 
In many cases, these algorithms provide the best theoretical runtimes or may even be the only tractable algorithms.
However, in large, these methods require consideration about their appropriateness for a given computational environment.



### Why this format?

Academic publishing is stuck using design choices that were made decades or centuries ago and are no longer relevant to the way information is created/consumed today 😞. 
In my opinion:
- Content creating and rendering should be though of as distinct tasks. 
This allows the content to be more easily rendered in a flexible manner (e.g. for different formats, devices, etc.)
Everyone knows how annoying it is trying to read a PDF meant for letter paper on a phone.
Separating content and rendering also helps with accessibility (PDFs are pretty bad for this).
- Content shouldn't be designed for print first.
Even with a requirement that the content be printable, we can still prioritize the much more common use-cases of reading on a computer or mobile device. Stuff like collapsible sections, hover-references, etc. can greatly improve the reading experience. 
Without a requirement for an "offline" version, we can also use interactive content (e.g. code snippets, interactive figures, etc.).
- With modern version control, we don't need to emphasize static content as much. By hosing documents online, we allow bugs/typos to be fixed more easily, while maintaining a history of changes.

Over the past few years, flexible technical document preparation formats (e.g. [MyST Markdown](https://mystmd.org) used in this document) are becoming more powerful, making a project like this viable.
This is partly my attempt to experiment with these new formats.

### Contributing

We welcome contributions and suggestions for improvement.
In particular readers can fix typos, update or add references/experiments/information, and suggest changes on [Github](https://github.com/tchen-research/RandNLA).
Larger contributions are also welcome, but please open an issue first so we can discuss how the content fits into the narrative before investing too much time.


### Citing this book

This book can currently be cited as:
```
@book{RandNLAwithExamples,
    title = {Randomized Numerical Linear Algebra with Examples},
    author = {Tyler Chen},
    year = {2025},
    version = {prerelease},
    url = {https://research.chen.pw/RandNLA},
}
```

## Other Resources

We are not aware of any other resources that provide (i) a broad introduction to RandNLA (ii) a large collection of numerical examples.
There are, however, many excellent resources on RandNLA, particularly for researchers.
The following surveys are of particular note:

- @martinsson_tropp_20: This survey describes many RandNLA algorithms that have a proven track record for real-world problem instances. The paper treats both the theoretical foundations of the subject and the practical computational issues. 

- @murray_etal_23: This survey explores randomized numerical linear algebra from a software development perspective, emphasizing the potential for standardized "RandBLAS" and "RandLAPACK" libraries to make these algorithms more accessible to practitioners. 

- @tropp_webber_23: This survey focuses specifically on randomized algorithms for computing low-rank matrix approximations. The work provides detailed non-asymptotic analyses of the performance of these algorithms and contains numerical examples to illustrate the effectiveness of the algorithms.

- @woodruff_14: This is an early book on sketching that provides a TCS-flavored overview of the field as of 2014. The focus is mostly on proving rates, and many of the key concepts in RandNLA are covered.

In addition, we highly recommend [Ethan Epperly's blog](https://www.ethanepperly.com/index.php/posts-by-topic/), which contains many informative posts on RandNLA topics, at both an introductory and research level, as well as numerical experiments and code snippets.



```{bibliography}
:filter: docname in docnames
```


