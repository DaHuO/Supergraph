#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import random

limit = 10000

def update(seen, n):
  for i in str(n):
    seen[int(i)] = 1

def solve(n):
  
  if n == 0:
    return False

  seen = [0] * 10
  i = 0
  current = n
  #print n
  while 1:
    i += 1
    if i > limit: break
    update(seen, current)

    if sum(seen) == 10:
      #print current, i
      return current

    current += n
    #print current
    
  return False

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
    tests.append(int(line.strip()))

if count != len(tests):
  print "Wrong number of test cases"
  sys.exit(0)

counter = 0
for n in tests:
  counter += 1
  #print t
  result = solve(n)
  print "Case #%d: %s" % (counter, "INSOMNIA" if result == False else str(result))
  #sys.exit()



