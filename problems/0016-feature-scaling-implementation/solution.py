import math
import numpy as np

def feature_scaling(data: np.ndarray) -> tuple:
    standardized_data = []
    normalized_data = []

    mediumarr = []
    vararr = []
    miniarr = []
    maxiarr = []

    for i in range(len(data[0])):
        med = 0
        var = 0
        mini = float('inf')
        maxi = float('-inf')

        for k in range(len(data)):
            med += data[k][i]
            mini = min(mini, data[k][i])
            maxi = max(maxi, data[k][i])

        med /= len(data)

        for k in range(len(data)):
            var += (data[k][i]- med) ** 2

        var /= len(data)
        var = math.sqrt(var)

        mediumarr.append(med)
        vararr.append(var)
        miniarr.append(mini)
        maxiarr.append(maxi)

    for i in range(len(data)):
        arrst = []
        arrmm = []
        for j in range(len(data[i])):
            if vararr[j] == 0:
                arrst.append(0)
            else:
                arrst.append(
                    (data[i][j] - mediumarr[j]) / vararr[j]
                )

            if maxiarr[j] == miniarr[j]:
                arrmm.append(0)
            else:
                arrmm.append(
                    (data[i][j] - miniarr[j])
                    / (maxiarr[j] - miniarr[j])
                )

        standardized_data.append(arrst)
        normalized_data.append(arrmm)

    return standardized_data,normalized_data