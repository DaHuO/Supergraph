#!/usr/bin/python
import sys
from collections import Counter

ipfile = sys.stdin
opfile = sys.stdout

T = int(ipfile.readline().strip())


for t in xrange(1,T+1):
    C, J = ipfile.readline().strip().split()
    l = len(C)
    maxval = int((10**(l)) - 1)
    mindiff = {}
    currmin = None
    for x in range(0, maxval+1):
      xs = str(x).zfill(l)
      xskip = False
      for idx in xrange(0,l):
        if C[idx] == "?":
          continue
        if C[idx]!=xs[idx]:
          xskip = True
          continue
      if xskip:
        continue

      for y in range(0, maxval+1):
        ys = str(y).zfill(l)
        yskip = False
        for idx in xrange(0,l):
          if J[idx] == "?":
            continue
          if J[idx]!=ys[idx]:
            yskip = True
            continue
        if yskip:
          continue

        diff = abs(x-y)
#        if currmin == None:
#          currmin = diff
#        if currmin>diff:
#          currmin=diff
        if diff not in mindiff:
          mindiff[diff] = []
        mindiff[diff].append((xs,ys,x,y))
    k = min(mindiff.keys())
    op = sorted(sorted(mindiff[k], key=lambda z: z[2]), key=lambda z: z[3])
    opfile.write('Case #%d: %s %s\n' % (t,op[0][0], op[0][1]))
