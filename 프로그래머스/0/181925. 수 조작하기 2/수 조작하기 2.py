def solution(numLog):
    answer = ''
    dic = { 1: "w", -1: "s", 10: "d", -10: "a" }
    for i,j in enumerate(numLog):
        if i != len(numLog)-1:
            answer += dic[numLog[i+1]-numLog[i]]
    return answer
        