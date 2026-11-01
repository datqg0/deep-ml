import numpy as np

def flip(a: np.ndarray) -> np.ndarray:
    """Reverse 1-D array a without slicing a[::-1]."""
    # Your code here
    out = []
    for i in range(len(a)-1,-1,-1):
        out.append(a[i])
    return np.array(out)
