def solution(n):
    a = n**0.5
    
    if a == int(a):
        return (a+1)**2
    else:
        return -1
    