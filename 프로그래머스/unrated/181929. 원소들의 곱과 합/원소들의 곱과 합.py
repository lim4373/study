def solution(num_list):
    answer = 0
    multiply = 1
    add = 0
    
    for i in num_list:
        multiply *= i
        add += i
    if   multiply < add*add:
        return 1
    else:
        return 0
    # answer = 1 if multiply < add*add else 0
    
    # return answer