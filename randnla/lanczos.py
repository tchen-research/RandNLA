import numpy as np
import scipy as sp
import time

def block_lanczos(H,V,k,reorth=True):
    """
    Input
    -----

    H    : d x d matrix
    V    : d x b starting block
    k    : number of iterations
    reorth : whether to apply reorthogonalization

    Returns
    -------
    Q1k  : First k blocks of Lanczos vectors
    Qkp1 : final block of Lanczos vetors
    A    : diagonal blocks
    B    : off diagonal blocks (incuding block for starting with non-orthogonal block)
    """
    if type(reorth) is bool:
        if reorth:
            reorth = k

    times = np.zeros(k+1)
    start = time.time()
    
    Z = np.copy(V)

    d = Z.shape[0]
    if np.shape(Z.shape)[0] == 1:
         b = 1
    else:
        b = Z.shape[1]

    A = [np.zeros((b,b),dtype=np.double)] * k
    B = [np.zeros((b,b),dtype=np.double)] * k

    Q = np.zeros((d,b*(k+1)),dtype=np.double)

    # B_0 accounts for non-orthogonal V and is not part of tridiagonal matrix
    Q[:,0:b],B_0 = np.linalg.qr(Z)

    times[0] = time.time() - start
    for j in range(0,k):

        Qj = Q[:,j*b:(j+1)*b]

        if j == 0:
            Z = H@Qj
        else:
            Qjm1 = Q[:,(j-1)*b:j*b]
            Z = (H @ Qj) - Qjm1 @ (B[j-1].conj().T)

        A[j] = Qj.conj().T @ Z
        Z -= Qj @ A[j]

        # double reorthogonalization 
        if reorth:
            Z -= Q[:,:(j+1)*b]@(Q[:,:(j+1)*b].conj().T@Z)
            Z -= Q[:,:(j+1)*b]@(Q[:,:(j+1)*b].conj().T@Z)

        Qjp1,B[j] = np.linalg.qr(Z)

        # double reorthogonalization in case QR factorization made stuff non-orthogonal to previous blocks
        # if reorth:
        #     Qjp1 -= Q[:,:(min(j+1,reorth_max))*b]@(Q[:,:(min(j+1,reorth_max))*b].conj().T@Qjp1)
        #     Qjp1 -= Q[:,:(min(j+1,reorth_max))*b]@(Q[:,:(min(j+1,reorth_max))*b].conj().T@Qjp1)
            
        Q[:,(j+1)*b:(j+2)*b] = Qjp1

        times[j+1] = time.time() - start

    # Q1k = Q[:,:b*k]
    # Qkp1 = Q[:,b*k:]

    return Q, (A, B, B_0), times


def get_block_tridiag(A,B):
    """
    Input
    -----

    A  : diagonal blocks
    B  : off diagonal blocks
        Without the first block B[0].

    Returns
    -------
    T  : block tridiagonal matrix
    """

    q = len(A)
    b = len(A[0])

    T = np.zeros((q*b,q*b),dtype=A[0].dtype)

    for k in range(q):
        T[k*b:(k+1)*b,k*b:(k+1)*b] = A[k]

    for k in range(q-1):
        T[(k+1)*b:(k+2)*b,k*b:(k+1)*b] = B[k]
        T[k*b:(k+1)*b,(k+1)*b:(k+2)*b] = B[k].conj().T

    return T

def get_banded_block_tridiag(A,B):

    q = len(A)
    b = len(A[0])

    ab = np.zeros((2*b+1,q*b))

    for i in range(q*b):
        for j in range(i,min(i+b+1,q*b)):
            x = i//b; u=i%b
            y = j//b; v=j%b

            if x==y:
                ab[b+j-i,i] = A[x][u,v]
                ab[b-j+i,j] = A[x][u,v]
            elif x==y-1:
                ab[b+j-i,i] = B[x].T[u,v]
                ab[b-j+i,j] = B[x].T[u,v]

    return ab