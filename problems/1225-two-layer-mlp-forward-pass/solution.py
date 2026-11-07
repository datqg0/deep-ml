import torch
import torch.nn as nn


def two_layer_mlp_forward(x, w1, b1, w2, b2):
    """Build a 2-layer MLP, set fixed weights, return scalar output.

    Args:
        x (torch.Tensor): Input of shape (1, 2).
        w1 (torch.Tensor): First Linear weight, shape (2, 2).
        b1 (torch.Tensor): First Linear bias, shape (2,).
        w2 (torch.Tensor): Second Linear weight, shape (1, 2).
        b2 (torch.Tensor): Second Linear bias, shape (1,).

    Returns:
        float: Scalar network output.
    """
    layer1 = nn.Linear(2, 2)
    layer2 = nn.Linear(2, 1)
    with torch.no_grad():
        layer1.weight.copy_(torch.tensor(w1))
        layer1.bias.copy_(torch.tensor(b1))
        layer2.weight.copy_(torch.tensor(w2))
        layer2.bias.copy_(torch.tensor(b2))
    x= layer1(x)
    x=torch.relu(x)
    return layer2(x).item()
