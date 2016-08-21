#!/usr/bin/python

import sys

T = int(sys.stdin.readline())

for i in range(0,T):
    N = int(sys.stdin.readline())
    if (N == 0):
        print ('Case #'+str(i+1)+': INSOMNIA')
        continue
    x = 0
    s = []
    num = 0
    while (num<10):
        x = x+N
        sX = str(x)
        for j in sX:
            if (not j in s):
                s.append(j)
                num += 1
            if (num == 10):
                print ('Case #'+str(i+1)+': '+str(x))
                break
