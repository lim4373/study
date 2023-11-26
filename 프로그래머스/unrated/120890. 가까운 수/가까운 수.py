def solution(array, n):
    answer = []
    array.sort()
    for i in array:
        answer.append(abs(n-i))
    answer = [array[answer.index(min(answer))]]
    if len(answer) > 1:
        return min(answer)
    else:
        return answer[0]