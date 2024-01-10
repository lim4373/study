# def solution(my_string, is_suffix):
#     answer = [my_string[i:] for i in range(len(my_string))]
#     return 1 if is_suffix in answer else 0


def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))