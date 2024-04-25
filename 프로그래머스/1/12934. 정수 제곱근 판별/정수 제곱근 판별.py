def solution(n):
    answer = n**0.5
    if answer % 1 ==0:
        return (answer+1)**2
    else:
        return -1