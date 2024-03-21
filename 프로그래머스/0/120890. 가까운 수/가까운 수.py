def solution(array, n):
    answer = []
    array.sort()
    for i in array:
        answer.append(abs(n-i))
    answer1 = [array[answer.index(min(answer))]]
    
    if len(answer1) > 1:
        return min(answer1)
    else:
        return answer1[0]