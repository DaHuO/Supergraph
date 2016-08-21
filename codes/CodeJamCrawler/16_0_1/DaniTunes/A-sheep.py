#!/bin/env python

# google code jam 2016 qualifiers problem 1
# Daniel Scharstein
import sys

def solve(n):
    if n == 0:
	return "INSOMNIA"
    a = set("0123456789")
    b = set()
    for k in range(1, 1000):
	kn = str(k*n)
	b |= set(kn)
	if a == b:
	    return kn
    print >> sys.stderr, "*************** not found", n
    return "INSOMNIA"

tests = int(raw_input())
for k in range(tests):
    n = int(raw_input())
    x = solve(n)
    print "Case #%d: %s" % (k+1, x)
