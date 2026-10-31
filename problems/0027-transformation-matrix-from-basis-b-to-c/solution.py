import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	A = np.array(B)
	B = np.array(C)
	if(np.linalg.det(B)==0):
		return -1
	return np.linalg.inv(B)@A