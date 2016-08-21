#!/usr/bin/sage -python

import sys
from sage.all import *

t = int(sys.stdin.readline())
n,j = map(int, sys.stdin.readline().split())

print 'Case #1:'
k = 0
for e in xrange(2**(n-2)):
  be = bin(e)[2:]
  be = '1' + '0'*(n-2-len(be)) + be + '1'

  l = []
  for b in xrange(2,11):
    t = int(be, b)
    if not is_prime(t):
      ft = factor(t)
      l.append(ft[0][0])
    else:
      break
  if len(l) == 9:
    print be, ' '.join(map(str,l))
    k+=1

  if k >= j:
    break
  
