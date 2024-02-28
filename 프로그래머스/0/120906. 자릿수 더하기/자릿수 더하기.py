def solution(n):
    answer = 0
    re = list(str(n))
    for i in re:
        answer+=int(i)       
    return answer