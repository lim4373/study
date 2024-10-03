def solution(arr, intervals):
    a,b = intervals[0]
    a1,b1 = intervals[1]
    print(a,b)
    return arr[a:b+1]+arr[a1:b1+1]