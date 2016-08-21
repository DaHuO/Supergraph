#!/usr/bin/python

import sys

def brute( S ):
    steps = 0
    while True:
        S = S.rstrip('+')
        if len(S) == 0:
            return steps
        if S[0] == '+':
            i = S.find('-')
            assert i >= 0
            S = '-'*i + S[i:]
        else:
            i = S.find('+')
            if i == -1:
                return steps + 1
            S = '+'*i + S[i:]
        steps = steps + 1

def brute2( S ):
    steps = 0
    while True:
        S = S.rstrip('+')
        if len(S) == 0:
            return steps
        if S[0] == '+':
            # flip from right
            S = S[::-1]
        else:
            # flip from left
            i = S.find('+')
            if i == -1:
                return steps + 1
            S = '+'*i + S[i:]
        steps = steps + 1

data = file(sys.argv[1]).read().splitlines()

NUMCASE = int(data.pop(0))

for CASE in xrange( 1, NUMCASE + 1 ):
    print 'Case #%d:' % ( CASE, ),
    S = data.pop(0)
    print brute( S )
    assert brute( S ) == brute2( S ) 

        
