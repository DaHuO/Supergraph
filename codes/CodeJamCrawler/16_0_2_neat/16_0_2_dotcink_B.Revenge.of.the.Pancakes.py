#!/usr/bin/env python

import sys

T = int(raw_input())
for t in range(1, T + 1):
  S = raw_input()
  s = []
  lastc = None
  for c in S:
    if lastc == None or c != lastc:
      lastc = c
      s.append(c)
  if s[-1] == '+':
    s[-1:] = []
  result = len(s)
  print "Case #%d: %d" % (t, result)
