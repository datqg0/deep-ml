def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	pass
	o = []
	if(len(a[0])!=len(b)):
		return -1
	for arr in a:
		sum = 0
		for i in range (len(arr)):
			sum+= arr[i]*b[i]
		o.append(sum)
	return o
