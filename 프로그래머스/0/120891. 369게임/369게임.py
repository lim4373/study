def solution(order):
    answer = 0
    c = ['3','6','9']
    for i in c:
        answer+=str(order).count(i)
    return answer