def solution(code):
    answer = ''
    mode = 0
    
    for i,j in enumerate(code):
        if j == "1":
            if mode == 1:
                mode = 0
            else:
                mode =1 
        if mode ==0:
            if i % 2 == 0 and j !="1":
                answer+=j
        else:
            if i % 2 ==1 and j !="1":
                answer+=j
    return answer if answer !="" else "EMPTY"