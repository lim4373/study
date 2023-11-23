def solution(num_list, n):
    answer = []
    cnt = 0
    asdf = []
    for num in num_list:
        asdf.append(num)
        cnt += 1
        if cnt == n:
            answer.append(asdf)
            asdf = []
            cnt = 0

    return answer