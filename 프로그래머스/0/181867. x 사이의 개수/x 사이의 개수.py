def solution(myString):
    answer = myString.split('x')
    print(answer)
    return [len(i) for i in answer]