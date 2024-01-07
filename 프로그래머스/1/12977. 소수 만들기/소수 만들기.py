import math, itertools

def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    sum_prime = []
    prime = itertools.combinations(nums,3)

    for i in prime:
        sum_prime.append(sum(i))

    for i in sum_prime:
        if isprime(i):
            answer +=1
    return answer