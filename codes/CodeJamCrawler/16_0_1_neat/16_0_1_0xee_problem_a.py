#!/bin/python

import sys


T = int(sys.stdin.readline())

l = [sys.stdin.readline() for i in range(T)]

Ns = [int(n) for n in l]

for i, N in enumerate(Ns):
    if N == 0:
        x = 'INSOMNIA'
    else:
        x = 0
        digits = []
        while len(digits) < 10:
            x = x + N
            for d in str(x):
                if d not in digits:
                    digits.append(d)

    print 'Case #%d: %s' % (i+1, str(x))
