def solution(arr, flag):
    answer = []
    for i,j in enumerate(arr):
        for k in range(j):
            if flag[i]:
                answer +=[j,j]
            else:
                answer.pop()
    return answer
