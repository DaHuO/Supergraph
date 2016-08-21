#!/usr/bin/env python
# -*- coding: utf-8 -*-

t = int(raw_input())  # read a line with a single integer

for index in xrange(1, t + 1):
  n = list(raw_input())
  out = []
  last = "A"

  for c in n:
    if len(out) == 0 or c >= out[0]:
      out.insert(0, c)
    else:
      out.append(c)

    last = c

  print "Case #{}: {}".format(index, ''.join(out))
