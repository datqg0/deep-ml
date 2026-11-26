import numpy as np
def activation_derivatives(x: float) -> dict[str, float]:
    """
    Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
    
    Args:
        x: Input value
        
    Returns:
        Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
    """
    # Your code here
    sigmoid  = 1/(1+np.exp(-x))
    dersigmoid = sigmoid*(1-sigmoid)
    tanh = np.tanh(x)
    dertanh = 1-tanh**2
    derrelu = 0
    if(x>0):
        derrelu=1
    return {'sigmoid':dersigmoid, 'tanh': dertanh, 'relu': derrelu }