import numpy as np
def precision(y_true, y_pred):
    # Your code here
    c = 0
    a=0
    for i in range (len(y_true)):
        if(y_true[i]==y_pred[i] and y_true[i]==1):
            c+=1
        if(y_pred[i]==1):
            a+=1
    if(a==0):
        return 0
    return c/a
