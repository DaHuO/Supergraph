from collections import deque
from itertools import permutations
inf = open('input.txt', 'r')
ouf = open('output.txt', 'w')

t = int(inf.readline())

for test in range(1, t + 1):
  print(test)
  n = int(inf.readline())
  l = list(map(int, inf.readline().split()))
  for i in range(n):
    l[i] -= 1
  a = []
  for i in range(1, n):
    a.append(i)
  ans = 0
  for i in range(2, n):
    for perm in permutations(a, i):
      perm = deque(perm)
      perm.appendleft(0)
      flag = False
      for k in range(len(perm)):
        if k == 0:
          if l[perm[k]] != perm[1] and l[perm[k]] != perm[-1]:
            flag = True
            break
        elif k < len(perm) - 1:
          if l[perm[k]] != perm[k - 1] and l[perm[k]] != perm[k + 1]:
            flag = True
            break
        else:
          if l[perm[k]] != perm[0] and l[perm[k]] != perm[k - 1]:
            flag = True
            break
      if not flag:
        ans = i + 1
        break
  a = []
  for i in range(1, n):
    a.append(i)
  for i in range(2, n):
    for perm in permutations(a, i):
      flag = False
      for k in range(len(perm)):
        if k == 0:
          if l[perm[k]] != perm[1] and l[perm[k]] != perm[-1]:
            flag = True
            break
        elif k < len(perm) - 1:
          if l[perm[k]] != perm[k - 1] and l[perm[k]] != perm[k + 1]:
            flag = True
            break
        else:
          if l[perm[k]] != perm[0] and l[perm[k]] != perm[k - 1]:
            flag = True
            break
      if not flag:
        ans = max(i, ans)
        break
  print('Case #', test, ': ', ans, sep = '', file = ouf)

inf.close()
ouf.close()
