#!/usr/bin/python
 
import sys
 
f = open("large2.in","rb")
t = int(f.readline())

def solve(st):
    count = 0
    cur = '+'
    n = len(st)-1
    for i in range(n,-1,-1):
         if (st[i] != cur):
             count+=1
             cur = st[i]
    return count

for i in range(t):
    st = f.readline().rstrip()

    out = solve(st)
    print "Case #%s:" % (i+1), out
