#!/usr/bin/env python

import sys
sys.stdin  = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w+')

T = int(input())
for t in range(T):
    S = str(input())
    i = len(S) - 1
    while i >= 0 and S[i] == '+':
        i -= 1
    if i < 0:
        print('Case', '#' + str(t + 1) + ':', '0')
        continue
    S = S[:(i + 1)]
    f = 0
    p = 0
    for i in range(len(S)):
        if (S[i] == '+' and f == 0):
            f = 1
            p += 1
        else:
            if (S[i] == '-'):
                f = 0
    z = 0
    if (len(S) > 1 and S[0] == '+'):
        z = -1
    #print('Case', '#' + str(t) + ':', len(S))
    print('Case', '#' + str(t + 1) + ':', p * 2 + 1 + z)
    

