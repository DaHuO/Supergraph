#!/usr/bin/python


import os
import sys


def solve(t):
    N = int(raw_input())
    if N == 0:
        print('Case #{}: INSOMNIA'.format(t))
    else:
        digits = set(str(N))
        n = N
        while len(digits) < 10:
            n += N
            digits.update(str(n))
        print('Case #{}: {}'.format(t, n))


def main():
    T = int(raw_input())
    for t in xrange(1, T+1):
        solve(t)


if __name__ == '__main__':
    main()

