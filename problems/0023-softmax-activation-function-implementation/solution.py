import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    maxi = max(scores)
    expo = [math.exp(x-maxi) for x in scores]
    sumo = sum(expo)
    return  [x/sumo for x in expo]