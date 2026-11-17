
import numpy as np
import math

def rmse(y_true, y_pred):
    # Write your code here
    if((y_pred.shape!=y_true.shape) or len(y_pred)==0):
         raise ValueError("Age cannot be negative")
    error = (y_true-y_pred)**2
    rmse_res = np.mean(error)
    rmse_res = math.sqrt(rmse_res)
    return round(rmse_res,3)
