def solution(my_string, s, e):
    answer = my_string[s:e+1][::-1]
    return my_string[:s]+answer+my_string[e+1:]