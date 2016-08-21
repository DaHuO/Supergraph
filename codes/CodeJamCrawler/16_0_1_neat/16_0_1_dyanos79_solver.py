#!/usr/bin/env python
import os,sys,string

problem = open(sys.argv[1], 'rt').readlines()

T = int(problem[0])
for order in range(0, T):
    n = int(problem[1+order])
    if n == 0:
        print "Case #%d: INSOMNIA" % (order + 1)
        continue
    digits = set([])
    for i in range(1, 200):
        v = "%d" % (i * n)
        for c in range(0, len(v)):
            ch = v[c]
            if int(ch) in digits:
                continue
            digits |= set([int(ch)])
        if len(digits) == 10:
            print "Case #%d: %s" % (order + 1, v) 
            break
    if len(digits) != 10:
        print "Case #%d: INSOMNIA" % (order + 1)
