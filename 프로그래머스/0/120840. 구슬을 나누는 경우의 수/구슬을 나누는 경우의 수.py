# from math import factorial as fac
# def solution(balls, share):
#     n = fac(balls)
#     m = fac(share)
#     bottom = fac(balls-share)*m
#     return n/bottom

import math
def solution(balls, share):
    return math.comb(balls,share)