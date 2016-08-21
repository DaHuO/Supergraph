#!/usr/bin/env python

import sys
sys.stdin  = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w+')

T = int(input())
for t in range(T):
    N = int(input())
    if N == 0:
        print('Case', '#' + str(t + 1) + ':', 'INSOMNIA')
        continue
    tN = N
    b = [0] * 10
    n = 1
    ok = False
    while n < 10 ** 6:
        for i in str(N):
            b[int(i)] = 1
        if b[0] == b[1] == b[2] == b[3] == b[4] == b[5] == b[6] == b[7] == b[8] == b[9] == 1:
            print('Case', '#' + str(t + 1) + ':', n * tN)
            ok = True
            break
        n += 1
        N = tN * n
    if not ok:
        print('Case', '#' + str(t + 1) + ':', 'INSOMNIA')
    
