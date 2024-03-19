def solution(my_string):
    answer = my_string.lower()
    a = sorted(answer)
    return "".join(a)