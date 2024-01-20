
def solution(babbling):
    can = ["aya", "ye", "woo", "ma" ]
    answer=0
    for i in babbling:
        for c in can:
            if c * 2 not in i:
                i = i.replace(c,'1')

        if i.isdigit():
            answer+=1
    return answer
