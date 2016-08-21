#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import random

def flip(s, n):

  #print "flipping", s, n
  result = ''
  for i in range(n):
    c = s[n-i -1]
    result += '-' if c == '+' else '+'

  result += s[n:]
  #print "result: ", result
  return result

def solve(s):

  flips = 0
  r = len(s) - 1
  #print s
  while r >= 0:
    if s[r] == '+':
      r -= 1
      continue
    elif s[0] == '+':
      c = 1
      while s[c] == '+':
        c += 1
      s = flip(s, c)
      flips += 1
      #print s

    s = flip(s, r + 1)
    flips += 1
    #print s
    r -= 1
  
  return flips

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
    tests.append(line.strip())

if count != len(tests):
  print "Wrong number of test cases"
  sys.exit(0)

counter = 0
for s in tests:
  counter += 1
  #print t
  print "Case #%d: %s" % (counter, solve(s))
  #sys.exit()



