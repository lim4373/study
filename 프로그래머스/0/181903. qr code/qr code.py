def solution(q, r, code):
    answer = ''
    for i,j in enumerate(code):
        if i % q == r:
            answer+=j
    return answer