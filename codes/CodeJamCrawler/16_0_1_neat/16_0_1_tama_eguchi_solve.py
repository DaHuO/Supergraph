#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem A. Counting Sheep
# https://code.google.com/codejam/contest/6254486/dashboard#s=p0
#

import sys
import random


def solve(N):
    digits = set()
    for k in range(1, 100):
        digits.update(str(k * N))
        if len(digits) >= 10:
            return k * N
    return 'INSOMNIA'


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        N = int(IN.readline().strip())
        OUT.write('Case #%d: %s\n' % (index + 1, solve(N)))


def makesample(T=100, Nmax=10 ** 6):
    print T
    for index in range(T):
        N = random.randint(0, Nmax)
        print N


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)
