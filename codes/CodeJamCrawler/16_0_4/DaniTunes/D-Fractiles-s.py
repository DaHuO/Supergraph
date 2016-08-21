#!/bin/env python

# google code jam 2016 qualifiers problem 4 small
# Daniel Scharstein

tests = int(raw_input())
for n in range(tests):
    k, c, s = map(int, raw_input().split())
    x = " ".join(map(str, range(1, k+1)))
    print "Case #%d: %s" % (n+1, x)
