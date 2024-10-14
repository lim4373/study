def solution(arr):
    count = 0
    a = len(arr)
    while a > 1:
        a = a/2
        count+=1
    return arr+[0]*(2**count-len(arr))