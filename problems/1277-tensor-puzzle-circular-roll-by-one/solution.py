import numpy as np

def roll(a: np.ndarray) -> np.ndarray:
    """Circular left shift by one."""
    # Your code here
    b = a.copy()
    for i in range(len(a)):
        b[i] = a[(i+1)%len(a)]
    return b
