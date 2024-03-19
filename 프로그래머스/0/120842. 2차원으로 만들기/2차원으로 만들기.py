import numpy as np
def solution(num_list, n):
    answer = np.array(num_list)
    answer = answer.reshape(-1,n)
    return answer.tolist()