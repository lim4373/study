def solution(price, money, count):
    sum_1 = 0
    answer = 0
    for i in range(1,count+1):
        sum_1 += i * price
        if sum_1 < money:
            answer = 0
        else:
            answer =  sum_1 - money
    return answer