#!/usr/bin/python
import re

L = []
T = int(input())
for i in range(1,T+1):
    pancakes = input()
    pancakes = pancakes.rstrip('+')
    numFlips = 0
    if pancakes:
        numFlips = 1
        side = pancakes[-1]
        for c in pancakes[::-1]:
            if c != side:
                side = c
                numFlips += 1
    L.append((i, numFlips))

for (x,y) in L:
    print("Case #%d: %d" % (x,y))
