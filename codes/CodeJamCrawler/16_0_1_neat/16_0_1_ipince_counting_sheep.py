#!/usr/bin/python

import sys

def solve(n):
  if n is 0:
    return None
  digits = set()
  factor = 1
  original_n = n
  while len(digits) < 10:
    n = factor * original_n
    digits.update(list(str(n)))
    #print "done checking %d ; digits are %s" % (n, sorted(digits))
    factor += 1
  return n


lines = iter(sys.stdin.readlines())
cases = int(lines.next())
for i in xrange(cases):
  n = int(lines.next())
  last_n = solve(n)
  if last_n:
    print "Case #%d: %s" % (i + 1, last_n)
  else:
    print "Case #%d: %s" % (i + 1, 'INSOMNIA')

