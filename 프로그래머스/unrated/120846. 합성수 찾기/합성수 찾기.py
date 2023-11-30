def solution(n):
    num = []
    a = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i%j == 0:
                num.append(i)
        if num.count(i)>= 3:
            a += 1
    return a
