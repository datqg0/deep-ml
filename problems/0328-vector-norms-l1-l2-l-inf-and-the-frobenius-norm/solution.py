import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    o = 0
    if(norm_type == 'l1'):
        arr = np.abs(arr)
        o = np.sum(arr)
    elif(norm_type == 'l2'):
        arr = arr**2
        o = np.sum(arr)
        o = np.sqrt(o)
    elif (norm_type == 'linf'):
        arr = np.abs(arr)
        o = np.max(arr)    
    else:
        if(arr.ndim==1):
            raise ValueError("arr must have 2 dimensions") 
        else:
            arr = arr**2
            o = np.sum(arr)
            o = np.sqrt(o)
    return o
    
