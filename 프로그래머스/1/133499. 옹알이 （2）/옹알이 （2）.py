def solution(babbling):
    answer = 0
    joka = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in joka:
            if j*2 not in i: # 연속되므로 발음할 수 없습니다. 
                i = i.replace(j,'1')
        if i.isdigit():
            answer+=1
    return answer