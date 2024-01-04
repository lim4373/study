import math
def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True   
def solution(n):
    answer = 0
    for i in range(2,n+1):
        if isprime(i) == True:
            answer +=1
    return answer