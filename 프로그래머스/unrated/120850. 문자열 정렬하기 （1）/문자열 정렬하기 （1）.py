def solution(my_string):
    answer = []
    for i in list(my_string):
        if i.isnumeric():
            answer.append(int(i))
    return (sorted(answer))
