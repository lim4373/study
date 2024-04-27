def solution(s):
    c = int(len(s)/2)
    if len(s)% 2 !=0:
        return s[c]
    else:
        return s[c-1:c+1]
    
    