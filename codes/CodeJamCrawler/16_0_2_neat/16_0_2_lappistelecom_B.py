#!/usr/bin/env python
#-*-coding: utf-8 -*-

def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

T = readint()

def count_p(s):
    res = 0
    for c in s:
        if c == '+':
            res += 1
    return res

for t in range(T):
    n = 0
    s = list(raw_input())
    while count_p(s) < len(s):
        n += 1
        c0 = s[0]
        found = False
        for i in range(len(s)):
            if s[i] != c0:
                i0 = i + 1
                found = True
                break
        if not found:
            i0 = len(s)
        if c0 == '-':
            c1 = '+'
        else:
            c1 = '-'
        for i in range(i0):
            s[i] = c1
    print "Case #%d: %d" % (t+1, n)
