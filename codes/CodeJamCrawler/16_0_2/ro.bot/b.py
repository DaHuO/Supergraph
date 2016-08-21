#!/usr/bin/python


import os
import sys


def solve(t):
    S = raw_input().strip()
    S += '+'
    p = S[0]
    count = 0
    for c in S[1:]:
        if c != p:
            count += 1
            p = c
    print('Case #{}: {}'.format(t, count))


def main():
    T = int(raw_input())
    for t in xrange(1, T+1):
        solve(t)


if __name__ == '__main__':
    main()

