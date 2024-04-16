def solution(arr, queries):
    answer = []
    a = []
    for s,e,k in queries:
        a = list(filter(lambda x:x>k,sorted(arr[s:e+1])))
        if len(a)>0:
            answer.append(a[0])
        else:
            answer.append(-1)
    return answer