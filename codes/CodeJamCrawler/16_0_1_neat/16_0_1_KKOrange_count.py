#!/usr/bin/python

import sys

N = map(int,sys.stdin.readlines())

idx = 0
for i in N[1:]:
    idx += 1
    if i == 0:
        print "Case #%d: INSOMNIA" % (idx)
        continue
    a = [False for x in range(10)]
    cur = 0
    while a.count(False) != 0:
        cur += i
        digits = str(cur)
        for c in digits:
            a[int(c)] = True
    print "Case #%d: %d" % (idx, cur)

