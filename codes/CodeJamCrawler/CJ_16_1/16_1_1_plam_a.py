#!/usr/bin/python

import sys

def isLast( A, B ):
    for i in xrange(0,len(A)):
        if A[i] > B[i]:
            return A
        if A[i] < B[i]:
            return B
    return A

def brute( S ):
    out = ''
    for i in xrange(0,len(S)):
        out = isLast( out + S[i], S[i] + out )
    return out

data = file(sys.argv[1]).read().splitlines()

NUMCASE = int(data.pop(0))

for CASE in xrange( 1, NUMCASE + 1 ):
    print 'Case #%d:' % ( CASE, ),
    S = data.pop(0)
    print brute(S)

        
