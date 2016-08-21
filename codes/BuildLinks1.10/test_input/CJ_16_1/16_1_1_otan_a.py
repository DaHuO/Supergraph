#!/usr/bin/python
import sys
T = int(sys.stdin.readline().strip())
for t in range(T):
  S = sys.stdin.readline().strip()
  o = ''
  for s in S:
    if len(o) == 0:
      o += s
    elif s >= o[0]:
      o = s + o
    else:
      o += s

  print("Case #%d: %s" % (t + 1, o))
