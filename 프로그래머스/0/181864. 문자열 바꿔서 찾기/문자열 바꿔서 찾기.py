def solution(myString, pat):
    answer = "".join(["B" if i == "A" else "A" for i in myString])
    return 1 if pat in answer else 0