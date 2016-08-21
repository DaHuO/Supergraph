#!/usr/local/bin/python3

from __future__ import print_function

T = int(input())
for t in range(1, T + 1):
    K, C, S = [int(a) for a in input().split(' ')]
    print('Case #', t, ':', sep='', end='')
    if C == 1 or K == 1:
        if S < K:
            print(' IMPOSSIBLE')
        else:
            for i in range(1, K + 1):
                print(' ', i, sep='', end='')
            print()
    else:
        if S < K - 1:
            print(' IMPOSSIBLE')
        else:
            for i in range(2, K + 1):
                print(' ', i, sep='', end='')
            print()


