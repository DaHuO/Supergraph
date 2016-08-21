#!/usr/bin/python

import string
import sys


def solve(i, stack):
    state = '+'
    flips = 0
    for ch in stack[::-1]:
        if ch != state:
            flips += 1
            state = ch
    print "Case #{}: {}".format(i, flips)


T = int(sys.stdin.readline())
for i in range(T):
    solve(i+1, sys.stdin.readline().strip())

