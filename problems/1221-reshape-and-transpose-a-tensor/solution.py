import torch

def reshape_transpose(t):
    """Reshape a 1D tensor of 6 elements to 2x3 (row-major) and return its transpose.

    Args:
        t (torch.Tensor): 1D tensor with exactly 6 elements.

    Returns:
        torch.Tensor: Transpose of the 2x3 reshape, with shape (3, 2).
    """
    # TODO: reshape to (2, 3) then transpose to (3, 2)
    pass
    #t = [1,2,3,4,5,6]
    t = torch.tensor(t)
    t = t.reshape(2,3)
    t = t.transpose(0,1)
    return t
