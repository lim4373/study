def solution(s):
    answer = 0
    slist = s.split()
    for i in range(len(slist)):
        if slist[i]=="Z":
            answer-=int(slist[i-1])
        else:
            answer+=int(slist[i])
    return answer