def solution(rsp):
    answer = {"2":"0","0":"5","5":"2"}
    result=""
    
    for move in rsp:
        result+=answer[move]
    return result