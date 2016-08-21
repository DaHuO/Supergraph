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

    N = int(raw_input())

    if N == 0:
        print 'INSOMNIA'
    else:
        res = 0
        s = set()

        i = 1
        while i<1e6 and len(s)<10:
            res += N
            s |= set(str(res))
            i+=1
        
        if len(s) == 10:
            print res
        else: 
            print 'INSOMNIA'
