def solution(a, b):
    if a % 2 == 1 and b % 2 == 1:
        return (pow(a, 2) + pow(b, 2))
    elif a % 2 == 1 or b % 2 == 1:
        return  (2 * (a + b))
    else:
        return  abs(a - b)