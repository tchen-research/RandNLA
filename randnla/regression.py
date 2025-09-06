import numpy as np
import scipy as sp

from .sketching import sparse_stack_sketch
from .factorization import randomized_cholesky_QR,sketched_qr


def randomized_cholesky_QR_regression_naive(A,b,k,zeta,rng):

    Q,R = randomized_cholesky_QR(A,k,zeta,rng)
    x = sp.linalg.solve_triangular(R,Q.T@b,lower=False)    

    return x

def randomized_cholesky_QR_regression(A,b,k,zeta,rng):

    Q1,R1 = sketched_qr(A,k,zeta,rng)
    X = Q1.T@Q1
    R2 = np.linalg.cholesky(X).T
    R = R2@R1
    y = sp.linalg.solve_triangular(R2.T,Q1.T@b,lower=True)
    x = sp.linalg.solve_triangular(R,y,lower=False)

    return x


