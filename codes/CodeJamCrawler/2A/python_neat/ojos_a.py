#!/usr/bin/env python

# R < P < S < R
# 0 < 1 < 2 < 0
Y = [[0, 2], [1, 0], [1, 2]]
W = ['R', 'P', 'S']

def so(C, N):
  nn = 2**N
  for i in xrange(N):
    p = 2**i
    step = 2*p
    for j in xrange(0, nn, step):
      A = C[j:j+p] 
      B = C[j+p:j+step]
      if A > B:
        C[j:j+p], C[j+p:j+step] = B, A
  return C

for nnn in xrange(1, int(raw_input())+1):
  print "Case #%d:" % (nnn),
  N, R, P, S = [int(x) for x in raw_input().split()]
  L = [R, P, S]

  candidates = []
  for winner in xrange(3):
    A = [winner]
    while True:
      if A.count(0)>=R and A.count(1)>=P and A.count(2)>=S:
        break
      A = [y for x in A for y in Y[x]] #flatten
    if A.count(0)==R and A.count(1)==P and A.count(2)==S:
      C = [W[x] for x in A]
      C = so(C, N)
      candidates.append(C)
      break
  if len(candidates) > 0:
    print ''.join([x for x in min(candidates)])
  else:
    print "IMPOSSIBLE"

