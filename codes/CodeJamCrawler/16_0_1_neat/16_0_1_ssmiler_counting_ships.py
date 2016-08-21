import sys
import math
import itertools as it
import operator as op
import fractions as fr

def digits(n):
  return set(map(int, str(n)))

t = int(sys.stdin.readline())
for i in range(1,t+1):
  n = int(sys.stdin.readline())

  k = -1
  d = digits(n)
  if n==0:
    r = 'INSOMNIA'
  else:
    r = n    
    for k in range(100):
      if len(d) == 10:
        break
      r += n
      d.update(digits(r))

  print('Case #{}: {}'.format(i, r))
  # print('Case #{}: {} the {}-th {}, digits'.format(i, r, k+1, len(d)))
  # print('{:3} {:10} {:3} {:3}'.format(n, r, k+1, len(d)))

