import torch
from torch.utils.data import TensorDataset, DataLoader

def batch_stats(X, y):
    """Wrap X and y in TensorDataset + DataLoader(batch_size=4, shuffle=False).

    Return (num_batches, first_batch_X_shape_tuple).
    """
    # TODO
    dataset = TensorDataset(X,y)
    loader = DataLoader(dataset,batch_size=4,shuffle=False)
    num_batch = len(loader)
    a,b = next(iter(loader))
    return num_batch,tuple(a.shape)
