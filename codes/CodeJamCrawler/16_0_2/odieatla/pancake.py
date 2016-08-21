#!/usr/bin/env python
# -*- coding: utf-8 -*-

t = int(raw_input())  # read a line with a single integer

for index in xrange(1, t + 1):
  n = list(raw_input())
  l = len(n)
  count = 0
  for i, c in enumerate(n):
    if c is '-':
      if i is (l-1):
        count += 1
        break
      if n[i+1] is '+':
        count += 1

    if c is '+':
      if i is (l-1):
        break
      if n[i+1] is '-':
        count += 1

  print "Case #{}: {}".format(index, count)


#execution
#python A.py < A-small-practice.in > result.txt
