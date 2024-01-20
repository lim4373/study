def solution(s):
    answer = []
    s_list= s[2:-2].split('},{')
    sorted_list=sorted(s_list, key=lambda x:len(x))
     # key 인자에 함수를 넘겨주면 우선순위가 정해짐
    for i in sorted_list:
        tp = i.split(',')
        answer.append(list(set(tp)-set(answer))[0])
    return [int(i) for i in answer]