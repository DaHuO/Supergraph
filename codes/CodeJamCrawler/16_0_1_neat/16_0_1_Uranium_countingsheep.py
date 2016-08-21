#!/usr/bin/env python2

def solve(n):
    if n == 0:
        return 'INSOMNIA'

    i = 1
    k = n
    digis = set(str(n))
    while len(digis) < 10:
        k = i*n
        i += 1
        digis.update(str(k))
    return k

T = int(raw_input())
for i in xrange(1, T+1):
    N = int(raw_input())
    print "Case #%s: %s" % (i, solve(N))
