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

def solve(K, C, S):
  return brute_force(K, C, S)

def run(original, C):
  result = original
  Gs = 'G' * len(original)
  for i in range(C-1):
    result = list(result)
    for p in range(len(result)):
      result[p] = Gs if result[p] == 'G' else original
    result = ''.join(result)
  return result

def replace(v):
  return v.replace('0', 'G').replace('1', 'L')

def gen(K, C):
  for i in range(2**K - 1):
    original = bin(i)[2:].ljust(K, '0')
    result = run(original, C)
    print(replace(original) + ': ' + replace(result))
  
def get_r(K, C, pos):
  if C == 1: return pos
  return K * (get_r(K, C-1, pos) - 1) + pos
  
def brute_force(K, C, S):
  if S < K: return 'IMPOSSIBLE'
  res = []
  max = K ** C
  
  for pos in range(1, K+1):
    #print('pos: %d' % pos)
    #r = (K**(C-1) * (pos-1) + pos)
    r = get_r(K, C, pos)
    #if r > max:
    #  import sys
    #  print('PANIC')
    #print('K: %d C: %d S: %d max: %d r: %d' % (K, C, S, max, r))
    #  sys.exit(1)
    res.append(r)
  return ' '.join(map(str, res))
  
if __name__ == '__main__':

  #gen(3, 4)
  #ans = brute_force(3, 2, 3)
  #print(ans)

  #import sys
  #sys.exit(0)
  
  T = readint()
  for t in range(1, T+1):
    K, C, S = map(int, input().split())
    ans = solve(K, C, S)
    print('Case #%d: %s' % (t, ans))