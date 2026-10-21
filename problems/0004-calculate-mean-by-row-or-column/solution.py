def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	row = [0 for v in range (len(matrix))]
	col = [0 for v in range (len(matrix[0]))]
	for i in range (len(matrix)):
		for j in range(len(matrix[0])):
			row[i]+= matrix[i][j]
			col[j]+= matrix[i][j]
	for i in range (len(row)):
		row[i] = row[i]/len(matrix[0])
	for j in range (len(col)):
		col[j] = col[j]/len(matrix)
	if(mode == 'column'):
		return col
	return row
			