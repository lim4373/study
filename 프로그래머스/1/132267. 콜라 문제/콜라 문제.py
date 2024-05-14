def solution(a, b, n):
    answer = 0
    while (n >= a):
        s = n % a
        n = (n //a) * b
        answer +=n
        n +=s
    return answer