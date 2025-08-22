import numpy as np

def lsqr(A,b,M,n_iters):

    n,d = A.shape

    x = np.zeros(d)
    u = np.copy(b)
    beta = np.linalg.norm(u)
    u /= beta
    
    v = M.T@(A.T@u)
    alpha = np.linalg.norm(v)
    v /= np.asarray(alpha)
    Mv = M@v
    w = Mv.copy()
    rhobar = alpha
    phibar = beta
    for t in range(n_iters):
        
        u *= -alpha
        u += A@Mv
        beta = np.linalg.norm(u)
        u /= beta
        
        v *= -beta
        v += M.T@(A.T@u)
        alpha = np.linalg.norm(v)
        v /= alpha
        
        rho = np.sqrt(rhobar**2 + beta**2)
        sn = beta / rho
        cs = rhobar / rho
        
        theta = sn * alpha
        rhobar = -cs * alpha
        phi = cs * phibar
        phibar = sn * phibar
        tau = sn * phi
        
        Mv = M@v
        dx = (phi / rho) * w
        
        x += dx
        
        w *= -theta / rho
        w += Mv
    
    return x