import numpy as np

def shuffle_data(X, y, seed=None):
    # Your code here
    if(seed != None):
        np.random.seed(seed)
    idx = np.random.permutation(len(y))
    X = X[idx]
    y = y[idx]
    return X,y
    