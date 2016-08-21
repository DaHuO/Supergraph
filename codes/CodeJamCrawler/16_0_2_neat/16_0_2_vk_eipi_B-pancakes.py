#!/usr/bin/python
import sys

def solve(S):
  cur = '+'
  flips = 0
  for ch in S[::-1]:
    if ch != cur:
      flips += 1
      cur = ch
  return flips

T = int(sys.stdin.readline())
for test_case in xrange(1, T+1):
  S = sys.stdin.readline().strip()
  ans = solve(S)
  print "Case #{0}: {1}".format(test_case, ans)
