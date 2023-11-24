import math

def solution(n):
    answer = 0
    while(n >= math.factorial(answer)):
        answer +=1
    return answer-1