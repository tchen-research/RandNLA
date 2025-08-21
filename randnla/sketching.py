import numpy as np
import scipy as sp


def gaussian_sketch(n,k,rng):
    S = rng.randn(k,n) / np.sqrt(k)
    return S

class trig_sketch():
    
    def __init__(self,n,k,rng):

        self.shape = (k,n)
        self.pi = rng.permutation(n)
        self.E = 2*rng.randint(0,2,n)-1
        self.R = rng.choice(n,size=k,replace=False)

    def __matmul__(self,A):

        A_loc = A.A if sp.sparse.issparse(A) else A
        return np.sqrt(self.shape[1]/self.shape[0])*sp.fft.dct(self.E[:,None]*A_loc[self.pi],norm='ortho',axis=0)[self.R]
    
def sparse_stack_sketch(n,k,zeta,rng):

    k_rem = k%zeta
    k_loc = k//zeta

    C = np.zeros((n,zeta),dtype=int)
    C[:,:k_rem] = np.random.randint(0,k_loc+1,size=(n,k_rem))
    C[:,k_rem:] = np.random.randint(0,k_loc,size=(n,zeta-k_rem))
    offsets = np.cumsum([0]+[k_loc+1]*k_rem + [k_loc]* (zeta-k_rem-1))
    C += offsets

    indices = C.flatten()
    values = np.sqrt(1/zeta)*(2*np.random.randint(2,size=n*zeta)-1)
    indptr = np.arange(0,n+1)*zeta
    S = sp.sparse.csc_matrix ((values,indices,indptr),shape=(k,n))

    return S