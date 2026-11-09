import torch
from torch.utils.data import TensorDataset, DataLoader

def batch_stats(X, y):
    """Wrap X and y in TensorDataset + DataLoader(batch_size=4, shuffle=False).

    Return (num_batches, first_batch_X_shape_tuple).
    """
    # TODO
    pass
    a = []
    p = []
    for i in range(len(X)):
        p.append((X[i],y[i]))
        if(len(p)==4):
            a.append(p.copy())
            p=[]
    if(len(p)>0):
        a.append(p.copy())
        p=[]
    num_batches = len(a)
    first_batch_X_shape = (len(a[0]), *X.shape[1:])

    return num_batches, first_batch_X_shape
