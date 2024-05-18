# def solution(n):
#     answer =0
#     for i in str(n):
#         answer +=int(i)
#     return answer



def solution(n):
    return sum(map(int, str(n)))