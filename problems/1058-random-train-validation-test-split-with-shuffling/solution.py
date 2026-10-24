import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    # Your code here
    pass
    n = len(data)
    rng = np.random.default_rng(seed)
    data = rng.permutation(data)
    #train
    number_of_train = int (int(n * train_frac))
    #validation
    number_of_val = int (int(n * validation_frac))
    #test
    number_of_test = n-number_of_train - number_of_val
    train = data[:number_of_train]
    valid = data[number_of_train:number_of_train + number_of_val]
    test = data[number_of_train + number_of_val:]

    return [train,valid,test]

    
