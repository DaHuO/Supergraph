#!/usr/bin/env python3

import sys


def solve(n):
    digits = set(map(int, str(n)))
    last_prefix = str(n)
    prefixes = [last_prefix]
    last_n = n
    steps = 1
    while True:
        last_n += n
        digits = digits.union(map(int, str(last_n)))
        if len(digits) == 10:
            return last_n
        x = str(last_n)
        if x in prefixes:
            return 'INSOMNIA'
        prefixes.append(x)
    return last_n


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in range(1, n + 1):
        m = int(sys.stdin.readline())
        print('Case #{}: {}'.format(i, solve(m)))
