import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    M=len(A)
    N=len(A[0])
    x=np.zeros((N,M))
    for j in range(N):
        for i in range(M):
            x[j][i]=A[i][j]
    return x
            
    
    # Write code here
    pass
