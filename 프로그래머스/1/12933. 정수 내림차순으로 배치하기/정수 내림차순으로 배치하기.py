def solution(n):
    answer= list(str(int(n)))
    answer.sort(reverse=True)
    return int("".join(answer))