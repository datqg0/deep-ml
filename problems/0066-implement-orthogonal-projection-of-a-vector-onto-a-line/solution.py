
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	pass
	a=0
	b=0
	o=[]
	for i in range (0,len(v)):
		a += v[i]*L[i] 
	for i in range (0,len(v)):
		b += L[i]*L[i]
	for i in range (0,len(v)):
		o.append(a/b*L[i])
	return o

