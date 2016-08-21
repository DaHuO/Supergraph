#!/usr/bin/python

import sys

N = int(sys.stdin.readline())

for i in range(0,N):
    pancakes = sys.stdin.readline().rstrip().rstrip('+')
    pancakes = list(pancakes)
    lp = len(pancakes)
    if (lp == 0):
        print ('Case #'+str(i+1)+': 0')
    else:
        flips = 0
        while (lp > 0):
            pc = []
            for p in pancakes:
                if (p != pancakes[0]):
                    break
                else:
                    if (p == '+'):
                        pc.append('-')
                    elif (p == '-'):
                        pc.append('+')
            pc = pc + pancakes[len(pc):]
            pancakes = list(''.join(pc).rstrip('+'))
            lp = len(pancakes)
            flips += 1
        print ('Case #'+str(i+1)+': '+str(flips))
