import math
from itertools import permutations
def isprime(x):
    if x < 2:
        return False
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x % i ==0:
                return False
    return True
def solution(numbers):
    answer = 0
    num=[]
    for i in range(1,len(numbers)+1):
        num +=list(set(map(''.join,permutations(numbers,i))))
    per = set(map(int,num))
    
    for p in per:
        if isprime(p):
            answer+=1
    return answer