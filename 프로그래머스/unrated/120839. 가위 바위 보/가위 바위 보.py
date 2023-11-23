def solution(rsp):
    game = {'2':'0', '0':'5','5':'2'}
    answer = ''
    for i in rsp:
        answer += game.get(i)
    return answer