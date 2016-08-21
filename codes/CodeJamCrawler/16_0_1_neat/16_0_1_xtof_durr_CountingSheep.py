#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# google code jam - c.durr - 2016
# CountingSheep

"""ad-hoc
"""

from sys import stdin


def readint(): return int(stdin.readline())
def readints(): return list(map(int, stdin.readline().split()))
def readstr(): return stdin.readline().strip()


def solve(N):
    if N == 0:
        return "INSOMNIA"
    else:
        sol = 0
        seen = [False] * 10
        tosee = 10
        val = 0
        while tosee > 0:
            sol += 1
            val += N
            for c in str(val):
                if not seen[int(c)]:
                    seen[int(c)] = True
                    tosee -= 1
        return val

for test in range(readint()):
    N = readint()
    print('Case #%d: %s' % (test + 1, solve(N)))
