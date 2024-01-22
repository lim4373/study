def solution(arr, delete_list):
    answer = []
    for i in arr:
        for j in delete_list:
            if i==j:
                answer.append(i)
                arr = [x for x in arr if x not in answer]
    return arr
        