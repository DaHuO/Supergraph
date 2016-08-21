#!/usr/bin/python

import sys

def digits( n ):
    out = set()
    while n:
        d = n % 10;
        n = n / 10;
        out.add( d )
    return out

def brute( n ):
    if n == 0:
        assert False
    o = set()
    s = n;
    while True:
        o.update( digits( s ) )
        if len( o ) == 10:
            return s;
        s = s + n

data = file(sys.argv[1]).read().splitlines()

NUMCASE = int(data.pop(0))

for CASE in xrange( 1, NUMCASE + 1 ):
    print 'Case #%d:' % ( CASE, ),
    N = int(data.pop(0))
    if N == 0:
        print 'INSOMNIA'
    else:
        print brute( N )

        
