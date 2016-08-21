#!/usr/bin/python

nb = int(raw_input())

for n in xrange(1, nb+1):
    K, C, S = [ int(i) for i in raw_input().split() ]

    if K == S:
        res = " ".join([ str(i) for i in xrange(1, K+1) ])
    else:
        res = "IMPOSSIBLE"

    print "Case #%i:" % (n), res
