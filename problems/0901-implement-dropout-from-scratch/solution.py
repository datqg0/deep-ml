import torch

def dropout(x: torch.Tensor, p: float, training: bool) -> torch.Tensor:
    if(training == False):
        return x
    mask = (torch.rand_like(x)>p).float()
    return x*mask/(1-p)
