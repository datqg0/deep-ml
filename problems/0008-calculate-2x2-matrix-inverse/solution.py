def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    pass
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    det = a*d - b*c
    #print (det)
    if(det==0):
        return None
    o = [[0.0,0.0],[0.0,0.0]]
    o[0][0] = round((1/det)*d, 2) 
    o[0][1] = round((1/det)*b*(-1), 2)
    o[1][0] = round((1/det)*(-1)*c, 2)
    o[1][1] = round((1/det)*a, 2) 
    return o