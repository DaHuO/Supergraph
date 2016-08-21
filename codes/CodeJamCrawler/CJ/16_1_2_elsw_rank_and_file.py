#/usr/bin/env python
# Google Code Jam Round 1A 2016
# B. Rank and File
# https://code.google.com/codejam/contest/4304486/dashboard#s=p1

t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    a = []
    for j in xrange(2*n-1):
        a += raw_input().split()
    heights = {}
    for height in set(a):
        heights[height] = a.count(height)
    out = []
    for height in heights:
        if heights[height] % 2 == 1:
            out.append(height)
    out.sort(key=int)
    print 'Case #%d: %s' % (i+1,' '.join(out))
