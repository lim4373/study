def solution(array, height):
    answer = 0
    for i in array:
        if height < i:
            answer+=1
        else:
            0
    return answer