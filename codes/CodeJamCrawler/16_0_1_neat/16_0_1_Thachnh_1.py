#!/usr/bin/python
 
import sys
 
f = open("large.in","rb")
t = int(f.readline())
global res

def solve(s, n):
    if s == 0:
        return "INSOMNIA"
    tmp = str(s)
    for i in tmp:
        res[int(i)] = True
    finish = True
    for i in range(10):
        if not res[i]:
            finish = False
            break
    if finish:
        return s
    else:
        return solve(s+n,n)
 
for i in range(t):
    n = int(f.readline())
    res = [False for ii in range(10)]

    out = solve(n,n)
    print "Case #%s:" % (i+1), out
