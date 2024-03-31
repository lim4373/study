def solution(myString):
    answer = [ i if i > "l" else "l" for i in myString]
    return ''.join(answer)
    