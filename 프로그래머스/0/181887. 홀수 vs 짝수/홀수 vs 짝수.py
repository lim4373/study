def solution(num_list):
    answer = 0
    answer1 = 0 
    for i in range(0,len(num_list),2):
        answer +=num_list[i]
    for j in range(1,len(num_list),2):
        answer1 +=num_list[j]
    return max(answer,answer1)