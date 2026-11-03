def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    pass
    mini = 99999999999999
    maxi = -99999999999999
    for i in range(len(x)):
        mini =min(mini,x[i])
        maxi =max(maxi,x[i])
    o = []
    for i in range(len(x)):
        o.append((x[i]-mini)/(maxi - mini))
    return o