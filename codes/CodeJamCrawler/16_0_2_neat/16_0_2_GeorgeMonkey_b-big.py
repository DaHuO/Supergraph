#!/bin/env python
from __future__ import print_function
import sys
import os
import os.path

fi = open(sys.argv[1], 'r')
fo = open(os.path.splitext(sys.argv[1])[0] + '.big.out', 'w')

T = int(fi.readline().strip())
for k in range(T):
    s = fi.readline().strip()
    c = 0
    lastchr = None
    for ch in s:
        if ch != lastchr:
            c += 1
            lastchr = ch
    if lastchr == '+':
        ret = c - 1
    else:
        ret = c
    print('Case #%d:' % (k + 1), ret, file=fo)

fi.close()
fo.close()
