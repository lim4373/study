def solution(babbling):
    answer = 0
    joka = ["aya", "ye", "woo", "ma" ]
    for i in babbling:
        for j in joka:
            if j*2 not in i:
                i = i.replace(j,' ')
        if i.isspace():
            answer+=1
    return answer