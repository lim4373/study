def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()

    for index_lost in range(len(lost)):
        for index_reserve in range(len(reserve)):
            if lost[index_lost] == reserve[index_reserve]:
                lost[index_lost] = -2
                reserve[index_reserve] = -2

    borrow = [False for _ in range(len(lost))]
    for index_lost, lst in enumerate(lost):
        if lost[index_lost] == -2:
            borrow[index_lost] = True
            continue

        for index_res, res in enumerate(reserve):
            if res == -2 or res == 0:
                continue

            if res == lst-1 or res == lst or res == lst+1:
                borrow[index_lost] = True
                reserve[index_res] = -2
                break

    answer = n - len([False for br in borrow if br is False])

    return answer
