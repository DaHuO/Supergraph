import os
import sys
import StringIO

inputs="""\
5
0
1
2
11
1692
"""
inf = StringIO.StringIO(inputs)

def solve(N):
  if N == 0: return "INSOMNIA"
  flags = [False]*10
  i = 1
  while i < 10000:
    n = i*N
    for m in str(n):
      flags[int(m)] = True
    if all(flags): return n
    i += 1
  return "INSOMNIA"

def nextVal():
  return sys.stdin.readline().rstrip('\n')
  #return inf.readline().rstrip('\n')

T = int(nextVal())
for t in range(1,T+1):
  N = int(nextVal())
  print "Case #%d: %s"%(t, solve(N),)
