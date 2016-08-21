#!/usr/bin/env pypy
# vim:ft=python:

from __future__ import print_function


def case(number, input):
    problem = next(input).strip()
    solution = ''
    for char in problem:
        candidate1 = solution + char
        candidate2 = char + solution
        if candidate1 < candidate2:
            solution = candidate2
        else:
            solution = candidate1

    print('Case #%i: %s' % (number, solution))


def main():
    from sys import stdin
    stdin = iter(stdin)
    next(stdin)  # first line useless
    case_number = 0
    try:
        while True:
            case_number += 1
            case(case_number, stdin)
    except StopIteration:
        return 0


if __name__ == '__main__':
    exit(main())
