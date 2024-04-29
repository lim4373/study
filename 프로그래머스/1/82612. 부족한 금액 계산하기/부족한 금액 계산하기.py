def solution(price, money, count):
    answer = []
    for i in range(1,count+1):
        answer.append(price*i)        
    if sum(answer)-money >0:
        return sum(answer)-money
    else:
        return 0