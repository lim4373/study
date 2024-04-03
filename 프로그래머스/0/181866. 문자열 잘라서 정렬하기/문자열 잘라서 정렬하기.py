def solution(myString):
    answer = list(filter(None,myString.split('x')))
    print(myString.split('x'))
    return sorted(answer)