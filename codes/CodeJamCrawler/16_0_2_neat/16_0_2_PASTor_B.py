#!/usr/bin/python

import sys, decimal as dec, collections as coll, itertools as itt, fractions as frac, math

if len(sys.argv) >= 2 and sys.argv[1] == 'debug':
    DEBUG = True
else:
    DEBUG = False




_T = int(raw_input())
_tt = max(_T/10, 1)

for _cc in xrange(_T):
    print 'Case #{}:'.format(_cc+1),
    if _cc % _tt == 0:
        print >>sys.stderr, 'Solving: ', (_cc+1)*100/_T, '%'

    s = raw_input()

    res = 0

    prev = s[0]
    for i in s:
        if i != prev:
            res += 1
            prev = i
            
    if s[-1] == '-':
        res += 1


    print res
