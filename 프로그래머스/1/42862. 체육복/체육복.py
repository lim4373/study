def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    answer = n

    reserve_and_lost = lost_set & reserve_set
    lost_set -= reserve_and_lost
    reserve_set -= reserve_and_lost

    for x in reserve_set:
        if x-1 in lost_set:
            lost_set.remove(x-1)
        elif x+1 in lost_set:
            lost_set.remove(x+1)

    answer -= len(lost_set)
    return answer