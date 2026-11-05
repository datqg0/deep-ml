import numpy as np

def kernel_function(x1, x2):
	# Your code here
	pass
	#tich vo hướng
	o = 0
	for i in range(len(x1)):
		o+=x1[i]*x2[i]
	return o