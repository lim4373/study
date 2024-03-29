def solution(my_string, is_prefix):
    answer = [my_string[:i] for i in range(0,len(my_string))]
    for j in answer:
        if is_prefix == j:
            return 1
    return 0