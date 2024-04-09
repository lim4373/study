def solution(bin1, bin2):
    answer = ''
    a = int(bin1,2)
    b = int(bin2,2)
    answer = bin(a+b)
    print(a,b,answer)
    return answer.replace("0b","")