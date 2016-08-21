#!/usr/bin/env python

import fileinput
import copy


def resolve(num):
    digits = set(str(num))
    mul = 2
    while len(digits) < 10:
        last = num * mul
        if last == num:
            return 'INSOMNIA'
        digits = digits.union(set(str(last)))
        mul += 1
    return last


if __name__ == "__main__":
    input = fileinput.input()
    nbtst = int(input.readline())
    for idx in range(nbtst):
        print 'Case #{}: {}'.format(idx+1, resolve(int(input.readline())))
