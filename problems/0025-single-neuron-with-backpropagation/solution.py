import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    # Your code here
    #forward
    z = labels.astype(float).copy()
    w = initial_weights.copy()
    b = initial_bias
    mse =0
    loss = []
    n = len(labels)
    for t in range (epochs):
        for i in range (len(features)):
            sum = 0
            for k in range(len(features[i])):
                sum += w[k]*features[i][k]
            sum+=b
            z[i] = sum
        sgm = 1/(1+np.exp(-z))
        sgmderivative = sgm * (1-sgm)

        #MSE loss calculation
        mse = 0
        for i in range (len(labels)):
            mse+=(sgm[i]-labels[i])**2
        mse/=n
        #backward 
        gradw = [0 for _ in range (len(w))]
        gradb = 0
        for i in range (len(features)):
            for j in range(len(features[i])):
                gradw [j]+=((sgm[i]-labels[i])*sgmderivative[i]*features[i][j])
        gradw = np.array(gradw)
        gradw*=2/n
        for j in range(n):
          gradb +=(sgm[j]-labels[j])*sgmderivative[j]
        gradb*=2/n
        #update 
        for j in range (len(w)):
            w[j] -= learning_rate*gradw[j]
        b -= learning_rate*gradb
        loss.append(mse)
    return w, b, loss