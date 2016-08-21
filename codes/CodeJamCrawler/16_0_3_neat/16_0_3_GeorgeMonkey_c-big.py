#!/bin/env python
from __future__ import print_function
import sys
import math
import os
import os.path
import random

DIVISOR_COUNT = 10000000

# divisors = {}

def test(s):
    global c, fo, J
    res = [s]
    for b in range(2, 11):
        n = int(s, b)
        found = False
        divisors = xrange(3, int(math.sqrt(n)))
        if len(divisors) > DIVISOR_COUNT:
            divisors = xrange(3, DIVISOR_COUNT + 3)
        if False:
            divisors = set()
            for cc in range(DIVISOR_COUNT):
                while True:
                    d = random.randrange(3, int(math.sqrt(n)), 2)
                    if d in divisors:
                        continue
                    divisors.add(d)
                    break
        for d in divisors:
            if n % d == 0:
                res.append(str(d))
                found = True
                break
        if not found:
            return
    print(' '.join(res), file=fo)
    c += 1
    print('%d:'%c, ' '.join(res))
    if c >= J:
        fi.close()
        fo.close()
        sys.exit()

def gen(s):
    global N
    if len(s) >= N:
        test(s)
    else:
        gen(s[:-1] + '0' + s[-1])
        gen(s[:-1] + '1' + s[-1])

fi = open(sys.argv[1], 'r')
fo = open(os.path.splitext(sys.argv[1])[0] + '.big.out', 'w')

T = int(fi.readline().strip())
for k in range(T):
    print('Case #%d:' % (k + 1), file=fo)
    v = fi.readline().strip().split()
    N = int(v[0])
    J = int(v[1])
    c = 0
    gen('11')

fi.close()
fo.close()
