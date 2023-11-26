def solution(cipher, code):
    answer = ''
    for i in range(code,len(cipher)+1):
        if i % code == 0:
            print(i)
            answer +=cipher[i-1]
    return answer