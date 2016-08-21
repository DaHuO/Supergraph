#!/usr/bin/python

import sys, decimal as dec, collections as coll, itertools as itt, fractions as frac, math



T = int(raw_input())
tt = max(T/10, 1)

for c in xrange(T):
    print 'Case #{}:'.format(c+1),
    if c % tt == 0:
        print >>sys.stderr, 'Solving: ', (c+1)*100/T, '%'

    K, C, S = map(int, raw_input().split())


    if int(math.ceil(K*1.0/C))>S:
        print 'IMPOSSIBLE'
    elif K == 1:
        print '1'
    else:
        res = ''
         
        m = 0
        for i in xrange(int(math.ceil(K*1.0/C))):
            
            power = 1
            for ii in xrange(C-1):
                power *= K
            
            # power = int(math.pow(K, C-1))
            pos = 1
            while power >= 1 and m < K:
                pos += m * power
                m += 1
                power /= K
                
            res += '{} '.format(pos)    

        if res[-1]==' ':
             res = res[:-1]
             
        print res


