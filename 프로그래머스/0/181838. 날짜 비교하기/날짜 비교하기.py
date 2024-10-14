def solution(date1, date2):
    answer = "".join(map(str,date1))
    answer1 = "".join(map(str,date2))
    
    if int(answer) < int(answer1):
        return 1
    return 0 
   