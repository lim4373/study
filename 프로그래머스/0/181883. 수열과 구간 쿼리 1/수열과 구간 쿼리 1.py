def solution(arr, queries):
    for i in queries:
        answer = [x+1 for x in arr[i[0]:i[1]+1]]
        arr[i[0]:i[1]+1] = answer
    return arr