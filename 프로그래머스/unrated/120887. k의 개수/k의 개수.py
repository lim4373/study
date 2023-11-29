def solution(i, j, k):
    answer = 0
    for p in range(i,j+1):
        if str(k) in str(p):
            answer +=str(p).count(str(k))
    return answer