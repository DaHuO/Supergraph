import sys
import math
import itertools as it
import operator as op
import fractions as fr

T = {'--': 0, '-+': 1, '+-': 1, '++': 0}

t = int(sys.stdin.readline())
for i in range(1,t+1):
  s = sys.stdin.readline().strip()

  r = 0
  if len(s) >= 1 and s[-1] == '-':
    r = 1
  for k in range(len(s)-1, 0, -1):
    r += T[s[k-1:k+1]]

  print('Case #{}: {}'.format(i, r))

