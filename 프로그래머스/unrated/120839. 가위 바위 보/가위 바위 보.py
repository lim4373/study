def solution(rsp):
    my_dict = {"2":"0", "0": "5", "5": "2"}
    answer =""
    for i in rsp:
        answer += my_dict.get(i)
    return answer