#!/usr/bin/python

nb = int(raw_input())

for n in xrange(1, nb+1):
    K, C, S = [int(i) for i in raw_input().split()]
    ll = [str(i) for i in xrange(1, S+1)]
    print "Case #%i:" % (n), " ".join(ll)  

