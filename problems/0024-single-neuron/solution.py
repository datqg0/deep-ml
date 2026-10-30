import math

def sigmoid(sum):
	pass
	return 1/(1+math.e**(-sum))
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	probabilities = []
	mse = 0
	z = []
	for i in range (len(features)):
		sum=0
		for j in range(len(features[i])):
			sum+= features[i][j]*weights[j]
		sum+=bias
		probabilities.append(round(sigmoid(sum), 4))
		z.append(sum)
	for i in range(len(labels)):
		mse += (probabilities[i]-labels[i])**2
	mse/=len(labels)
	mse = round(mse, 4)
	return probabilities, mse