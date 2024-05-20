import numpy as np
def solution(n):
    answer = np.sqrt(n)
    if answer % 1 == 0:
        return (answer+1)**2
    return -1