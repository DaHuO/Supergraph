#!/usr/bin/python

import sys

d = {}

for i, s in enumerate(sys.stdin.readlines()[1:]):
    print "Case #%d:" % (i+1),
    n = int(s)
    if n == 0:
        print "INSOMNIA"
        continue
    if n in d:
        print d[n]
    else:
        x = 0
        f = set()
        while len(f) < 10:
            x += n
            f = f.union(set(str(x)))
        print x
        d[n] = x
