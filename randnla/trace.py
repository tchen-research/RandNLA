import numpy as np
import scipy as sp


def girard_hutchinson(A,m):

    n,_ = A.shape

    X = np.random.randn(n,m)
    trm = np.mean(np.diag(X.T@(A@X)))

    return trm
    


def hutchpp(A,m):

    m1 = (m+2)//4
    m2 = m - 2*m1 
    n,_ = A.shape

    Ω = np.random.randn(n,m1)
    Q,_ = np.linalg.qr(A@Ω,mode='reduced')
    Z = A.T@Q
    trB = np.sum(np.diag(Z.T@Q)) 

    X = np.random.randn(n,m2)    
    trm = np.mean(np.diag(X.T@(A@X) - (X.T@Q)@(Z.T@X)))

    return trB + trm