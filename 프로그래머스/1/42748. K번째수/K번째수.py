def solution(array, commands):
    answer = []
    for i,j,k in commands:
        a = sorted(array[i-1:j])
        answer.append(a[k-1])
    return answer