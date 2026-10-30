import numpy as np
import math

def log_softmax(scores: list) -> np.ndarray:
    maxi = max(scores)
    o = []

    expo = [math.exp(x - maxi) for x in scores]
    sumo = sum(expo)

    for i in range(len(scores)):
        o.append(scores[i] - maxi - math.log(sumo))

    return np.array(o)