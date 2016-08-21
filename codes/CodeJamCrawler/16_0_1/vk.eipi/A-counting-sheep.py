#!/usr/bin/python
import sys

LIMIT = 1000

def bruteforce(n):
  if n == 0:
    return "INSOMNIA"
  seen = set()
  for i in xrange(1,LIMIT+1):
    num = i*n
    seen.update(str(num))
    if len(seen) == 10:
      return num
  return "ERROR"

T = int(sys.stdin.readline())
for test_case in xrange(1, T+1):
  N = int(sys.stdin.readline())
  answer = bruteforce(N)
  print "Case #{0}: {1}".format(test_case, answer)
