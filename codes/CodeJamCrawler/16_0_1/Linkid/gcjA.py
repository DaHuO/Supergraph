#!/usr/bin/env python
# -*- coding: utf-8 -*

"""GCJ 2016 Qualification Round: Problem A."""


DIGITS_SET = set(range(10))


def solve(n):
    digits = set()
    number = 0

    while digits != DIGITS_SET:
        number += n
        sheeps = set(str(number))
        sheeps_int = [int(sheep) for sheep in sheeps]
        digits.update(sheeps_int)

    return number


if __name__ == "__main__":
    T = int(input())  # nb of test cases
    default = "INSOMNIA"

    for x in range(T):
        N = int(input())

        if N == 0:
            y = default
        else:
            y = solve(N)
        print("Case #%d: %s" % (x + 1, y))
