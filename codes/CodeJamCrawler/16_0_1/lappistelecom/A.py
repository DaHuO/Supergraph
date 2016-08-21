#!/usr/bin/env python
#-*-coding: utf-8 -*-

def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

T = readint()

for t in range(T):
    N = readint()
    seen = set()
    i = 1
    out = False
    if N == 0:
        s = "INSOMNIA"
        out = True
    while not out:
        a = N * i
        for c in str(a):
            seen.add(int(c))
            if len(seen) >= 10:
                s = a
                out = True
                break
        i += 1
    print "Case #%d: %s" % (t+1, s)
