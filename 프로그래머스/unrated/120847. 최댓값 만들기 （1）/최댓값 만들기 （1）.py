def solution(numbers):
    numbers.sort()
    a = numbers[-1:]
    b = numbers[-2:-1]
    for i in a:
        for j in b:
            return i*j