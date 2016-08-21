#!/usr/bin/python2
from sys import stdin



def solve(n):
    if n==0:
        return "INSOMNIA"
    s = set()
    value = n
    while len(s)<10:
        cur = str(value)
        for c in cur:
            s.add(c)
        value += n
    return value - n


lines = int(stdin.readline())
for i in range(1,lines+1):
    l = int(stdin.readline())
    print "Case #%d: %s" % (i,solve(l))