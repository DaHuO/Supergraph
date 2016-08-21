#!/usr/bin/env python
# -*- coding:utf-8 -*-

def readint(): return int(input())
def readfloat(): return float(input())
def readarray(N, foo):
        res = []
        for _ in xrange(N):
                res.append(foo())
        return res
def readlinearray(foo): return map(foo, input().split())

def solve(N):
  if N == 0: return 'INSOMNIA'
  s = set()
  c = 1
  while len(s) != 10:
    n = c * N
    #print(n)
    s = s.union(list(str(n)))
    #print(s)
    c += 1
  return str(n)
  
if __name__ == '__main__':

  #for i in range(10**6):
  #  solve(i)
  #print('OK')
  #import sys
  #sys.exit(0)
  
  T = readint()
  for t in range(1, T+1):
    N = readint()
    ans = solve(N)
    print('Case #%d: %s' % (t, ans))