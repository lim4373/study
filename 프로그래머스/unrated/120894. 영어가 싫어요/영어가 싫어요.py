def solution(numbers):
    answer = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for index,answer in enumerate(answer):
        numbers = numbers.replace(answer,str(index))
    return int(numbers)