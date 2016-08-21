N = int(input())
J = int(input())

import random

F = set()
S = list()
while len(S) < J:
  l = [1] + [random.randint(0, 1) for i in range(N-2)] + [1]
  d = []
  ok = True
  for p in range(2, 11):
    nb = 0
    for i,x in enumerate(l):
      nb += x * pow(p, i)
    div = -1
    for i in range(2, 11):
      if (nb % i) == 0:
        div = i
    d.append(div)
  if -1 not in d:
    x = "".join([str(x) for x in reversed(l)])
    y = " ".join([str(x) for x in d])
    if x in F:
      continue
    F.add(x)
    S.append(x + " " + y)

for s in S:
  print(s)
