import math

def prime(x):
    if x<=1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for num in range(2,n+1):
        if prime(num):
            answer+=1
    return answer