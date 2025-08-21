import numpy as np
import scipy as sp

from .sketching import sparse_stack_sketch

def cholesky_QR(A):

    X = A.T@A
    R = np.linalg.cholesky(X).T
    Q = sp.linalg.solve_triangular(R.T, A.T, lower=True).T

    return Q, R

def sketched_qr(A,k,zeta,rng):

    n, d = A.shape
    S = sparse_stack_sketch(n,k,zeta,rng) 
    Y = S @ A 
    R = np.linalg.qr(Y, mode='r') 
    Q = sp.linalg.solve_triangular(R.T,A.T,lower=True).T 
    
    return Q, R

def randomized_cholesky_QR(A,k,zeta,rng):

    Q1, R1 = sketched_qr(A,k,zeta,rng)
    Q, R2 = cholesky_QR(Q1)
    R = R2 @ R1
    
    return Q, R