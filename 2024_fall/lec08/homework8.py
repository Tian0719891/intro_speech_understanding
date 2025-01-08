import numpy as np

def dft_matrix(N):
    """
    Create a DFT transform matrix, W, of size N.
    
    @param:
    N (scalar): number of columns in the transform matrix
    
    @result:
    W (NxN array): a matrix of dtype='complex' whose (k,n)^th element is:
           W[k,n] = cos(2*np.pi*k*n/N) - j*sin(2*np.pi*k*n/N)
    """
    # Create indices for rows and columns
    k = np.arange(N).reshape((N, 1))  # Column vector
    n = np.arange(N).reshape((1, N))  # Row vector
    
    # Compute the (k,n)^th element
    W = np.exp(-2j * np.pi * k * n / N)
    return W
