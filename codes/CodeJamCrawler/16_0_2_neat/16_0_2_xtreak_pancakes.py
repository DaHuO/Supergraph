#!/usr/bin/python3

import sys
import re

def solve(case):
    strlen = len(case)
    if case == '-' * strlen:
        return 1
    elif case == '+' * strlen:
        return 0
    elif re.match('^-+\++$', case):
        return 1
    elif re.match('^\++-+$', case):
        return 2
    elif re.match('^\++-+\++$', case):
        return 2
    elif re.match('^(?P<match>-+\++)', case):
        k = re.match('^(?P<match>-+\++)', case)
        start, end = k.start(), k.end()
        case = '-' * end + case[end:]
        return 2 + solve(case)
    elif re.match('^(?P<match>\++)-+', case):
        k = re.match('^(?P<match>\++)-+', case)
        start, end = k.start(), k.end()
        case = '-' * end + case[end:] 
        return 1 + solve(case)


number_of_test_cases = int(sys.stdin.readline())
k = 1
for line in sys.stdin:
    string = line.strip()
    solution = str(solve(string))
    print("Case #{}: {}".format(k, solution))
    k += 1
