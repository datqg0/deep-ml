import numpy as np
import math
def mae(y_true, y_pred):
    """
    Calculate Mean Absolute Error between two arrays.

    Parameters:
        y_true (numpy.ndarray): Array of true values
        y_pred (numpy.ndarray): Array of predicted values

    Returns:
        float: Mean Absolute Error
    """
    # Your code here
    pass
    o = 0
    y_true = y_true.flatten()
    y_pred = y_pred.flatten()
    for i in range(0,len(y_true)):
        o+= abs(y_true[i]-y_pred[i])
    return o/len(y_true)