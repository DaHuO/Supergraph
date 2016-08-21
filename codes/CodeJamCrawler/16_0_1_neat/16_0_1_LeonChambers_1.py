#!/usr/bin/env python3
import math

t = int(input())
cases = [int(input()) for i in range(t)]

def digits(n):
    while int(n) > 0:
        yield n % 10
        n = math.floor(n / 10)

for case_num in range(len(cases)):
    case = cases[case_num]
    if case == 0:
        print('Case #{}: INSOMNIA'.format(case_num+1))
        continue
    curr = case
    digits_left = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    i = 1
    while len(digits_left):
        curr = case * i
        digits_left = digits_left - set(list(digits(curr)))
        i += 1
    print("Case #{}: {}".format(case_num+1, curr))
