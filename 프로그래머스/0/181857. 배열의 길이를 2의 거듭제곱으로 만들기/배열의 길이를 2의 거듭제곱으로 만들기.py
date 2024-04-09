def solution(arr):
    count = 0
    answer = len(arr)
    while answer > 1:
        answer /=2
        count+=1
    return arr+[0]*(2**count-len(arr))