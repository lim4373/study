def solution(myString, pat):
    count = 0
    index = myString.find(pat)

    while index != -1:
        count += 1
        index = myString.find(pat, index + 1)

    return count