def solution(emergency):
    answer = []
    answer1 = []
    answer1 = sorted(emergency, reverse = True)
    
    for i in emergency:
        answer.append(answer1.index(i)+1)
    return answer