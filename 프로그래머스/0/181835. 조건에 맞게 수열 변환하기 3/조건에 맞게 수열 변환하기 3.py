def solution(arr,k):
    answer=[]
    for i in arr:
        if k % 2 == 1:
            answer.append(i*k)
        else:
            answer.append(i+k)
    return answer
            


# def solution(arr, k):
#     if k % 2 !=0:
#         return list(map(lambda x:x*k,arr))
#     return list(map(lambda x:x+k,arr))
    


