import numpy as np

def make_diagonal(x):
	# Your code here
	o = []
	for i in range (len(x)):
		a = [0 for i in range(len(x))]
		a[i] = x[i]
		o.append(a)
	return o