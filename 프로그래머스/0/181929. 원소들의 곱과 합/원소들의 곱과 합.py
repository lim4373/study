def solution(num_list):
    sum_ = 0
    multi = 1
    
    for i in num_list:
        multi *= i
        sum_ += i
        
    if multi  < sum_ **2:
        return 1
    return 0