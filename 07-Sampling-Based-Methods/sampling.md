---
title: Sampling-Based Methods
description: Strategic sampling approaches for matrix operations including importance sampling, CUR decomposition, and adaptive methods
keywords: [sampling-based methods, importance sampling, leverage scores, CUR decomposition, sparse matrices, distributed computing, adaptive sampling]
numbering:
  equation:
    enumerator: 7.%s
  proof:theorem:
    enumerator: 7.%s
  proof:algorithm:
    enumerator: 7.%s
  proof:definition:
    enumerator: 7.%s
  proof:proposition:
    enumerator: 7.%s
---


This this chapter, we discuss algorithms that rely on subsampling the input. 
In many ways, such algorithms are conceptually different from the mixing-based methods described in previous chapters. 
In particular, sampling based methods don't necessarily need to read the whole input and can therefore often achieve *sublinear* runtimes. 
This makes them particularly enticing for massive problems that might otherwise be intractable. 