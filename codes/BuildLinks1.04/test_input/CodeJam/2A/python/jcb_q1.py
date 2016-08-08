#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import random

best = {"R":[("R",(1, 0, 0))], "S": [("S",(0, 0, 1))], "P": [("P",(0, 1, 0))]}

def order(x, y):
  if x < y:
    return x, y
  return y, x

def add_tuple(x, y):
  return tuple([x[i] + y[i] for i in range(len(x))])

N = 12

for i in range(1, N+1):
  #R
  a, b = order(best["R"][i-1], best["S"][i-1])
  best["R"].append((a[0] + b[0], add_tuple(a[1], b[1])))

  #P
  a, b = order(best["P"][i-1], best["R"][i-1])
  best["P"].append((a[0] + b[0], add_tuple(a[1], b[1])))

  #S
  a, b = order(best["S"][i-1], best["P"][i-1])
  best["S"].append((a[0] + b[0], add_tuple(a[1], b[1])))
 
#print best

def solve(t):
  N, R, P, S = t
  candidate = None
  for c in best:
    if best[c][N][1] == (R, P, S):
      if candidate == None or best[c][N][0] < candidate:
        candidate = best[c][N][0]

  
  return "IMPOSSIBLE" if not candidate else candidate

total = None
count = 0
f = sys.stdin

count = None
tests = []
for line in sys.stdin:
  if not count:
    count = int(line.strip())
    continue
  else:
    tests.append([int(x) for x in line.strip().split()])

if count != len(tests):
  print "Wrong number of test cases"
  sys.exit(0)

counter = 0
for s in tests:
  counter += 1
  #print t
  print "Case #%d: %s" % (counter, solve(s))
  #sys.exit()



