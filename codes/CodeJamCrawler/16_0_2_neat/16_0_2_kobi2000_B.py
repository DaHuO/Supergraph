import os
import sys
import StringIO

inputs="""\
5
-
-+
+-
+++
--+-
"""
inf = StringIO.StringIO(inputs)

def solve(S):
  cnt = 0
  s = S[0]
  if len(S) > 0:
    for ix in range(1, len(S)):
      if S[ix] != s:
        cnt += 1
        s = S[ix]
  return cnt + (s == '-')

def nextVal():
  return sys.stdin.readline().rstrip('\n')
  #return inf.readline().rstrip('\n')

T = int(nextVal())
for t in range(1,T+1):
  S = nextVal()
  print "Case #%d: %s"%(t, solve(S),)
