#!/usr/bin/env python

import sys
T = int(raw_input())

for i in range(T):
  N = int(raw_input())
  result = 0
  if N != 0:
    left = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    already = []
    count = 1
    while len(left) > 0:
      current = count * N
      for c in str(current):
        if c not in already:
          left.remove(c)
          already.append(c)
      count += 1
    result = (count - 1) * N
  if result == 0:
    print "Case #%d: INSOMNIA" % (i + 1)
  else:
    print "Case #%d: %d" % (i + 1, result)
