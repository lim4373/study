def solution(numbers):
    answer = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i,j in enumerate(answer):
        numbers = numbers.replace(j, str(i))
    return int(numbers)