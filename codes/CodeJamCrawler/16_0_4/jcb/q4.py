#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import random

def convert(buf, k):

  #print buf, k
  result = 0
  for i in xrange(len(buf)):
    if buf[i] > 0:
      result += buf[i] * k**i
  #print result + 1
  return result + 1

def solve(k, c, s):

  if s * c < k:
    return False

  needed = k / c
  if needed * c < k:
    needed += 1 

  results = [[0] * c for i in xrange(needed)]
  current = k-1
  for i in range(c):
    for j in range(needed):
      results[j][i] = current
      current -= 1
      if current <= 0: break
    if current <= 0: break

  return [convert(i, k) for i in results]

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
  #print "Wrong number of test cases"
  sys.exit(0)

counter = 0
for k, c, s in tests:
  counter += 1
  #print t
  solution = solve(k, c, s)
  #print solution
  if solution == False:
    print "Case #%d: IMPOSSIBLE" % (counter,)
  else:
    print "Case #%d: %s" % (counter, " ".join([str(l) for l in solution]))
  #sys.exit()



