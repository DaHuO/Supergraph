#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# google code jam - c.durr - 2016
# Coin Jam
# greedy, complexity O(n) -- why is input only n<=100 ? suspicious

from sys import stdin


def readint(): return int(stdin.readline())
def readints(): return list(map(int, stdin.readline().split()))
def readstr(): return stdin.readline().strip()


def solve(N, J):
    for i in range(J):
        pattern = bin(i)[2:]
        t = ['1'] * 2 + ['0'] * (N - 4) + ['1'] * 2
        for j in range(len(pattern)):
            t[2 + 2 * j    ] = pattern[-j-1]
            t[2 + 2 * j + 1] = pattern[-j-1]
        s = ''.join(t)
        print(s, end='')
        # check
        for base in range(2, 11):
            x = int(s, base)
            assert x % (base + 1) == 0
            print(' %i' % (base + 1), end='')
        print()

for test in range(readint()):
    N, J = readints()
    print('Case #%d:' % (test+1))
    solve(N, J)

