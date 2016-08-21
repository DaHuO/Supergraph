# -*- coding: utf-8 -*-

import sys


def count_flips(pancakes):
    flips = 0
    cur_pancake = pancakes[0]
    for pancake in pancakes:
        if pancake != cur_pancake:
            flips += 1
            cur_pancake = pancake
    if pancakes[-1] == '-':
        flips += 1
    return flips


def main():
    num_cases = int(sys.stdin.readline())
    cases = [sys.stdin.readline().strip() for _ in range(num_cases)]
    for case_num, case in enumerate(cases):
        print('Case #{}: {}'.format(case_num + 1, count_flips(case)))


if __name__ == '__main__':
    main()
