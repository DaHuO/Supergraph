#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
from __future__ import unicode_literals


#===============================================================================
def read_input(strip=True):
    return raw_input().strip() if strip else raw_input()


def read_input_multi(strip=True):
    return read_input(strip).split()


def read_int():
    return int(read_input())


def read_int_multi():
    return [int(s) for s in read_input_multi()]


def print_solution(i, solution):
    print('Case #{}: {}'.format(i, solution))
#===============================================================================

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
order_d = [0, 2, 6, 8, 3, 4, 5, 7, 1, 9]

#------------------------------------------------------------------------------


def solve():
    s = read_input().lower()
    num = []
    for current in order_d:
        d = digits[current]
        while all(l in s for l in d):
            num.append(current)
            for l in d:
                s = s.replace(l, '', 1)
    num.sort()
    return ''.join([str(n) for n in num])


#===============================================================================
if __name__ == '__main__':
    test_cases = read_int()
    for t in xrange(test_cases):
        solution = solve()
        print_solution(t + 1, solution)
