import numpy as np

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
	# Your code here
	Wh = np.array(Wh)
	Wx = np.array(Wx)
	b = np.array(b)
	now = np.array(initial_hidden_state)
	final_hidden_state = now
	for i in range (len(input_sequence)):
		#wx*xi
		a= np.array(input_sequence[i])
		p = Wx@a +Wh@now + b
		p = np.array(p)
		p = np.tanh(p)
		now = p
		final_hidden_state = p
	return final_hidden_state