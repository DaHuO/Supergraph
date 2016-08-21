#!/usr/bin/python
import sys

def solve(S):
  chars = list(S)
  output = []
  last = len(chars)
  while last > 0:
    ch, last = max((chars[i], i) for i in xrange(last))
    output.append(chars.pop(last))
  output.extend(chars)
  return "".join(output)

T = int(sys.stdin.readline())
for test_case in xrange(1, T+1):
  S = sys.stdin.readline().strip()
  ans = solve(S)
  print "Case #{0}: {1}".format(test_case, ans)
