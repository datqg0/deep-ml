import torch

def softmax(t, dim):
    """Numerically stable softmax along dim.

    Args:
        t (torch.Tensor): input tensor
        dim (int): dimension along which to apply softmax

    Returns:
        torch.Tensor: tensor of same shape as t; slices along dim sum to 1
    """
    # TODO: subtract max along dim, exp, then normalize
    pass
    max_vals = torch.max(t, dim=dim, keepdim=True).values
    e = torch.exp(t-max_vals)
    se = torch.sum(e,dim=dim,keepdim=True)
    o = e/se
    return o
