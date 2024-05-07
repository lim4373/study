def solution(s):
    answer = []
    sd ={}
    
    for i in range(len(s)):
        if s[i] not in sd:
            answer.append(-1)
        else:
            answer.append(i-sd[s[i]])
        sd[s[i]]=i
    return answer