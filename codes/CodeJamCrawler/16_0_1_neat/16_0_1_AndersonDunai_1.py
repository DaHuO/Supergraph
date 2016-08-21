#!/usr/bin/env python2

import sys

count = int(sys.stdin.readline().strip())
case = 1


def solve(arg):
    if arg == 0:
        return 'INSOMNIA'

    current = arg

    v = set(str(current))
    mul = 0

    while len(v) < 10:
        mul += 1
        current = arg * mul
        v = v | set(str(current))

    return current

while case <= count:
    arg = int(sys.stdin.readline().strip())
    print 'Case #{}: {}'.format(case, solve(arg))
    case += 1
