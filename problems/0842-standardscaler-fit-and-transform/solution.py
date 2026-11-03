import numpy as np
import math
def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """
    Fit a standard scaler on X_train and transform X_test.
    Returns the standardized X_test as a numpy array.
    """
    #meancal
    mean_arr = []
    standard_arr  =  []
    for i in range (len(X_train[0])):
        mean = 0
        for j in range (len(X_train)):
            #mean = mean
            mean += X_train[j][i]
        mean_arr.append(mean/len(X_train))
    
    for i in range (len(X_train[0])):
        standard = 0
        for j in range (len(X_train)):
            #standard = standard
            standard += (X_train[j][i]-mean_arr[i])**2
        standard/=len(X_train)
        standard = math.sqrt(standard)
        if(standard == 0):
            standard=1
        standard_arr.append(standard)

    o = []
    for i in range (len(X_test)):
        q = []
        for j in range(len(X_test[0])):
            q.append ((X_test[i][j]-mean_arr[j])/standard_arr[j])
        o.append(q)
    return o

    
