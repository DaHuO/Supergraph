#! /usr/bin/env python

"""
1000000110000001
       100000001

"""

def bin(n, d):
    s = ''
    for i in xrange(d):
        n, r = divmod(n, 2)
        s = str(r) + s
    return s

print "Case #1:"

N, J = 32, 500
dd = N / 2
d = dd - 2
for i in xrange(J):
    lol = '1' + bin(i, d) + '1'
    lol = lol + lol
    print lol, ' '.join([str(b ** dd + 1) for b in xrange(2, 11)])
