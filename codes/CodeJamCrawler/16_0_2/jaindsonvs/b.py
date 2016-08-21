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

def reverse(S, n):
  S = list(S)
  for i in range(n + 1):
    S[i] = '+' if S[i] == '-' else '-'
  return ''.join(S)

def solve(S):
  n = 0
  expected = len(S) * '+'
  while True:
    if S == expected: break
    next = S.rindex('-')
    S = reverse(S, next)
    n += 1
  return n
  
if __name__ == '__main__':
  T = readint()
  for t in range(1, T+1):
    S = input()
    ans = solve(S)
    print('Case #%d: %d' % (t, ans))