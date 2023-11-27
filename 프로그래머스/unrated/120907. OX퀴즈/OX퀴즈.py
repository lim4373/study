def solution(quiz):
    answer = []
    for s in quiz:
        a = s.split(' ')
        if eval(''.join(a[:3])) == int(a[-1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer