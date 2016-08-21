import sys
import math
import itertools as it
import operator as op
import fractions as fr

# def f(s, c):
#   r = s
#   for _ in range(c):
#     rn = ''
#     for c in r:
#       if c == 'G':
#         rn += 'G' * len(s)
#       else:
#         rn += s
#     r = rn
#   return r

# r = []
# for s in l:
#   r.append(map(lambda e: {'L': 0, 'G': 1}[e], f(s,c)))
# r = np.array(r)


t = int(sys.stdin.readline())
for p in range(1,t+1):
  k,c,s = map(int, sys.stdin.readline().split())

  if s <= k-c:
    r = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(p, r))
  else:
    l = list(range(1,k+1))
    c = min(c, k)
    for i in range(c-1):
      for j in range(i+1,k):
        l[j] = (l[i]-1) * k + j + 1

    r = l[(c-1):]

    print('Case #{}: {}'.format(p, ' '.join(map(str,r))))


