#!/usr/bin/env python
#-*-coding: utf-8 -*-

def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

T = readint()

for t in range(T):
    K, C, S = readarray(int)
    if K == S:
        print "Case #%d: %s" % (t+1, ' '.join(map(str, range(1, K+1))))
