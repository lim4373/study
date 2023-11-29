def solution(dots):
    dots.sort(key=lambda x: (x[0], x[1]))
    return abs(dots[0][0] - dots[3][0]) * abs(dots[0][1] - dots[3][1])