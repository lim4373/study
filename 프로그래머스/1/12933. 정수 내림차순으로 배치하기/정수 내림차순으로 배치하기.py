def solution(n):
    n = list(str(int(n)))
    n.sort(reverse = True)
    return int("".join(n))