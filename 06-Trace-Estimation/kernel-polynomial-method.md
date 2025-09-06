---
title: Kernel Polynomial Method
description: Alternative method to Stochastic Lanczos Quadrature for spectral density approximation using Chebyshev moments with smooth function approximation
keywords: [kernel polynomial method, KPM, spectral density, Chebyshev moments, smooth approximation, physics applications]
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

The Kernel Polynomial Method is a popular alternative to SLQ, particularly in physics; see e.g. {cite:p}`weisse_wellein_alvermann_fehske_06`.
As with SLQ, the KPM approximates $\phi(x;\vec{A})$ by approximating the Chebyshev moments.
However, the resulting approximation is now a smooth function (as opposed to a sum of Dirac delta functions).
Similar theoretical convergence guarantees are available {cite:p}`chen_trogdon_ubaru_25,chen_24`.