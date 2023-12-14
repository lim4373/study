def solution(number):
    a = len(number)
    answer = 0
    for i in range(len(number)):
        for j in range(i+1,a):
            for k in range(j+1,a):
                if number[i]+number[j]+number[k] == 0:
                    answer+=1
    return answer