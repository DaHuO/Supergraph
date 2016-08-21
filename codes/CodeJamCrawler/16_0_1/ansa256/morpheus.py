#!/usr/bin/env python3

import sys

def morpheus(n):
  c = 0
  d = set()

  while (len(d) != 10):
    c += n
    d = d | set(str(c))

  return c

file = open(sys.argv[1])

total = int(file.readline())

for i in range(1, total + 1):
  n = int(file.readline())
  r = "INSOMNIA" if n == 0 else morpheus(n)
  print("Case #%d: %s" % (i, r))