# -*- coding: utf-8 -*-

import sys


def count_sheeps(num):
    if num == 0:
        return 'INSOMNIA'
    digits = set()
    count = num
    for c in str(count):
        digits.add(c)
    while len(digits) < 10:
        count += num
        for c in str(count):
            digits.add(c)
    return count


def main():
    num_cases = int(sys.stdin.readline())
    cases = [int(sys.stdin.readline()) for _ in range(num_cases)]
    for case_num, case in enumerate(cases):
        print('Case #{}: {}'.format(case_num + 1, count_sheeps(case)))


if __name__ == '__main__':
    main()
