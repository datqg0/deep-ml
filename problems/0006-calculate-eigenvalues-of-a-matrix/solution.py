import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a1 = matrix[0][0]
    b1 = matrix[0][1]
    c1 = matrix[1][0]
    d1 = matrix[1][1]
    a = 1
    b = -(a1+d1)
    c = a1*d1 - c1*b1 
    delta = b*b -4*a*c 
    eigenvalues = []
    if(delta==0 ):
        eigenvalues = [-b/2*a,-b/2*a]
    elif(delta>0):
        eigenvalues = [(-b+math.sqrt(delta))/2*a,(-b-math.sqrt(delta))/2*a]
    eigenvalues.sort(reverse=True)
    return eigenvalues