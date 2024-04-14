def solution(strArr):
    answer = [len(i) for i in strArr]
    a = []
    for j in set(answer):
        a.append(answer.count(j))        
    return max(a)