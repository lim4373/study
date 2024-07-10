def solution(common):
    one, two, three = common[:3]
    if two-one == three- two:
        return common[-1]+(two-one)
    elif two // one == three//two:
        return common[-1]*(two//one)