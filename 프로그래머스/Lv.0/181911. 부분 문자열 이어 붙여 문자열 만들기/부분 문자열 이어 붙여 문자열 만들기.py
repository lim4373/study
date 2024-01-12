def solution(my_strings, parts):
    answer = ''
    
    for i,k in enumerate(parts):
        answer +=my_strings[i][k[0]:k[1]+1]
    return answer