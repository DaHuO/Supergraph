#!/usr/bin/env python2

import sys

n, j = map(int, raw_input().split())
print "Case #1:"
for i in xrange(j):
    t = bin(2 ** (n/2 - 1)+1 + 2 * i)[2:] * 2
    print t, ' '.join(str(b ** (n/2) + 1) for b in xrange(2, 11))
