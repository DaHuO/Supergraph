#!/usr/bin/env python3


import sys
import re
import itertools
import collections


BOARD_REGEX = re.compile(r"\?")


def get_cases():
    num_cases = int(sys.stdin.readline())
    for _ in range(num_cases):
        yield sys.stdin.readline().split()


def solve_case(case):
    return min(itertools.product(substs_for_score(case[0]),
                                 substs_for_score(case[1])),
               key=lambda x: abs(int(x[0]) - int(x[1])))


def substs_for_score(score):
    combos = itertools.product(range(10), repeat=score.count('?'))
    combos = ("".join(map(str, combo)) for combo in combos)

    for combo in combos:
        current = score
        remaining = collections.deque(combo)
        while remaining:
            current = BOARD_REGEX.sub(remaining.popleft(), current, count=1)
        yield current


def main():
    for index, case in enumerate(get_cases(), start=1):
        print("Case #{}: {} {}".format(index, *solve_case(case)))


if __name__ == '__main__':
    main()
