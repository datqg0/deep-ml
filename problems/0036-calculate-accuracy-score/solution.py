import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	pass
	c = 0 
	for i in range (len(y_true)):
		if(y_pred[i]==y_true[i]):
			c+=1
	return c/len(y_pred)