def solution(a, d, included):
    return sum((a+d*i)*int(included[i]) for i in range(len(included)))