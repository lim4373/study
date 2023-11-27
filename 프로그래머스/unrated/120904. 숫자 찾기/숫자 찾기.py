def solution(num, k):
    answer = 0
    str_num = str(num)
    for i in str_num:
        answer +=1
        if i == str(k):
            return answer
    return -1
    return answer