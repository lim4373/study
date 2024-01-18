from functools import cmp_to_key

def compare(a,b):
    if a[1]==b[1]:
        return a[0]-b[0]
    
    return b[1]-a[1]

def solution(N, stages):
    answer = []
    total =len(stages)# 사용자의 수
    fails = []
    users= [0 for _ in range(N+1)]
    for s in stages:
        users[s-1]+=1

    for i in range(N): #i가 각 스테이지 번호
        if users[i]==0:
            fails.append((i+1,0))
        else:
            fails.append((i+1,users[i]/total)) #users[i]현재 스테이지의 사용자수 
            total-=users[i]

    for f in sorted(fails,key=cmp_to_key(compare)):
        answer.append(f[0])
    return answer