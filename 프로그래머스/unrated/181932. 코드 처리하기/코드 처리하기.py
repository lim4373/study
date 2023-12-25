def solution(code):
    answer = ''
    mode = 0
    

    for idx, val in enumerate(code):
        if val == "1":
            mode = 0 if mode == 1 else 1
        if mode == 0:
            if idx % 2 == 0 and val != "1":
                answer += val
        else:
            if idx % 2 == 1 and val != "1":
                answer += val
    
    return answer if answer!="" else "EMPTY"