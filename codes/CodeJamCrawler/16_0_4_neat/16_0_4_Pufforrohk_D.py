#!/usr/bin/python2
from sys import stdin
from string import rstrip
from math import pow

def solve(k,c,s):
    if s<k:
        return "IMPOSSIBLE"
    d = k ** (c-1)
    return " ".join([str(d*i+1) for i in range(k)])



lines = int(stdin.readline())
for i in range(1,lines+1):
    k,c,s = map(int,rstrip(stdin.readline()).split(" "))
    print "Case #%d: %s" % (i,solve(k,c,s))