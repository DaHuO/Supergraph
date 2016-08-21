#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def solve(t, i):
  res = t[0]
  for c in t[1:]:
    if c > res[0]:
      res = c + res
    elif c < res[0]:
      res += c
    else:
      k = 1
      while k < len(res) and c <= res[k]:
        k += 1
      if k < len(res):
        res = c + res
      else:
        res += c
  print 'Case #%d: %s'%(i, res)

if __name__ == "__main__":
  with open(sys.argv[1]) as f:
    buf = f.read()
  t = buf.split("\n")
  nb_tests = int(t[0])
  t = t[1:]
  for k in xrange(0, nb_tests):
    solve(t[k], k+1)
