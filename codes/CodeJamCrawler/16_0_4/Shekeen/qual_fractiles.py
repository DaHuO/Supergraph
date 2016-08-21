# -*- coding: utf-8 -*-

import sys


def solve_small_fractile(k, c, s):
    period = k ** (c - 1)
    return ' '.join(str(1 + i * period) for i in range(s))


def main():
    num_cases = int(sys.stdin.readline())
    cases = [tuple(map(int, sys.stdin.readline().split())) for _ in range(num_cases)]
    for case_num, case in enumerate(cases):
        print('Case #{}: {}'.format(case_num + 1, solve_small_fractile(*case)))


if __name__ == '__main__':
    main()
