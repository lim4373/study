def solution(phone_number):
    answer = len(phone_number)
    back = phone_number[-4:]
    return "*"*(answer-4)+back