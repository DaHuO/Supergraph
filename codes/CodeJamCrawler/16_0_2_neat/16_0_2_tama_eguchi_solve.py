#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem B. Revenge of the Pancakes
# https://code.google.com/codejam/contest/6254486/dashboard#s=p1
#

import sys
import random
import string

fliptable = string.maketrans('-+', '+-')


def flip(S, count):
    # Sの先頭count個をflipしたものを返す
    return string.translate(S[:count], fliptable) + S[count:]


def lensame(S):
    for index, c in enumerate(S):
        if c != S[0]:
            return index
    return len(S)


def solve(S):
    goal = '+' * len(S)
    count = 0
    while S != goal:
        size = lensame(S)
        S = flip(S, size)
        count += 1
    return count


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        S = IN.readline().strip()
        OUT.write('Case #%d: %s\n' % (index + 1, solve(S)))


def makesample(T=100, Smax=100):
    print T
    for index in range(T):
        Slength = random.randint(1, Smax)
        print ''.join(random.choice('+-') for n in range(Slength))


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)
