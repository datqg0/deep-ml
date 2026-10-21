import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	n = len(a)
	m = len(a[0])
	if(n*m != new_shape[0]*new_shape[1]):
		return []
	reshaped_matrix=[]
	t =[]
	for arr in a:
		for v in arr:
			t.append(v)
			if(len(t)==new_shape[1]):
				reshaped_matrix.append(t)
				t=[]
	return reshaped_matrix