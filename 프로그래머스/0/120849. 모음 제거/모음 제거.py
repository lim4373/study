def solution(my_string):
    remove_=['a', 'e', 'i', 'o', 'u']
    for i in remove_:
        my_string = my_string.replace(i,'')        
    return my_string