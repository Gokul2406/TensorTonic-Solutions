import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    num_rows, num_cols = A.shape
    transpose = np.zeros((num_cols, num_rows))
    for i in range(num_cols):
        transpose[i, :] = A[:, i]
    return transpose
    