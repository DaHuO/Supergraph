#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(n):
  if n == 0: return 'INSOMNIA'
  sum = n
  s = set(str(sum))
  while len(s) < 10:
    sum += n
    s.update(set(str(sum)))
  return sum

if __name__ == "__main__":
	for case in xrange(1, 1+input()):
		print "Case #{0}: {1}".format(case, solve(input()))