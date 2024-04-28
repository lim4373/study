import math

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        sqrt = math.sqrt(i)
        if int(sqrt) == sqrt:
            answer -= i
        else:
            answer += i

    return answer