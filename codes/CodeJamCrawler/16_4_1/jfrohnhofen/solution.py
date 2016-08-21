#!/usr/bin/python

from sys import stdin as I

def split(X, N):
  while X:
    yield X[:N]
    X = X[N:]

def s(X):
  L = X[:len(X)/2]
  R = X[len(X)/2:]
  if L < R:
    return L + R
  else:
    return R + L

def solve(N, W):
  L = {
    'R': 'RS',
    'P': 'PR',
    'S': 'SP'
  }
  for _ in range(N):
    W = ''.join(map(lambda w: L[w], W))

  for _ in range(N):
    L = 2**(_+1)
    P = list(split(W, L))
    P = map(s, P)
    W = ''.join(P)

  return ((N, W.count('R'), W.count('P'), W.count('S')), W)

C = {}

for N in range(1, 14):
  for W in ['R', 'P', 'S']:
    K, V = solve(N, W)
    C[K] = V

T = int(I.readline())
for i in range(T):
    K = tuple(map(int, I.readline()[:-1].split(' ')))
    if K in C:
      print "Case #%d: %s" % (i+1, C[K])
    else:
      print "Case #%d: IMPOSSIBLE" % (i+1)
