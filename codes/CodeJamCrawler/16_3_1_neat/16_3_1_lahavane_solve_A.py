#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

ab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def enter(d):
  res = []
  k = 0
  while len(d.keys()) > 1:
    a, b = d.keys()[0:2]
    res.append(a+b)
    d[a] -= 1
    d[b] -= 1
    for k in d.keys():
      if d[k] == 0:
        d.pop(k)
  if len(d.keys()) == 1:
    a = d.keys()[0]
    while d[a] > 1:
      res.append(a+a)
      d[a] -= 2
    if d[a] == 1:
      res.append(a)
  return res


def solve(t, i):
  N = int(t[2*i])
  P = map(int, t[2*i+1].split(' '))
  d = {}
  for k in xrange(N):
    d[ab[k]] = P[k]
  res = enter(d)
  res.reverse()
  print 'Case #%d: %s'%(i+1, ' '.join(res))

if __name__ == "__main__":
  with open(sys.argv[1]) as f:
    buf = f.read()
  t = buf.split("\n")
  nb_tests = int(t[0])
  t = t[1:]
  for k in xrange(0, nb_tests):
    solve(t, k)
