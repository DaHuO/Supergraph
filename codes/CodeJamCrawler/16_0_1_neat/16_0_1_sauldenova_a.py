#!/usr/bin/python

from __future__ import print_function

T = int(raw_input())
for t in range (1, T + 1):
    res = [False for i in range(10)]
    N = int(raw_input())
    print('Case #', t, ': ', sep='', end = '')
    if N == 0:
        print('INSOMNIA')
    else:
        idx = 1
        for digit in [int(i) for i in str(N)]:
            res[digit] = True

        while not all(res):
            idx += 1
            for digit in [int(i) for i in str(N * idx)]:
                res[digit] = True

        print(N * idx)
