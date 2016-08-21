#!/usr/bin/python

import sys

data = file(sys.argv[1]).read().splitlines()

NUMCASE = int(data.pop(0))

for CASE in xrange( 1, NUMCASE + 1 ):
    print 'Case #%d:' % CASE,
    ( k, c, s ) = [ int(x) for x in data.pop(0).split() ]
    assert k == s
    for i in xrange(1, s + 1):
        print i,
    print

