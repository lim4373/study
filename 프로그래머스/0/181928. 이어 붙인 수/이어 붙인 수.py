def solution(num_list):
    answer = ''
    answer1= ''
    for i in num_list:
        if i%2 !=0:
            answer+=str(i)
        else:
            answer1+=str(i)
    return int(answer)+int(answer1)
