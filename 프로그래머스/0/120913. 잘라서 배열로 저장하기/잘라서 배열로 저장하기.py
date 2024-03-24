def solution(my_str, n):
    return [my_str[i:n+i] for i in range(0,len(my_str),n)]