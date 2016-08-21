#!/usr/bin/env python3
"""https://code.google.com/codejam/contest/6254486/dashboard"""
import fileinput

stdin = fileinput.input()
T = int(next(stdin))

ALL_DIGITS = frozenset('0123456789')

for case_no in range(1, T+1):
    N = int(next(stdin))
    if N == 0:
        print('Case #{}: {}'.format(case_no, 'INSOMNIA'))
    else:
        current_number = N
        seen_digits = set(str(N))
        i = 2
        while seen_digits != ALL_DIGITS:
            current_number = i * N
            for digit in str(current_number):
                seen_digits.add(digit)
            i += 1
        print('Case #{}: {}'.format(case_no, current_number))
