def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse = True)
    
    for i in range(0,len(score),m):
        apple = score[i:i+m]
        if len(apple)==m:
            answer += min(apple)*m
    return answer