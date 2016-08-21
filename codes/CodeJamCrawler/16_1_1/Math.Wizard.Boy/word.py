from sys import stdin
from collections import deque

T = int(stdin.readline())

for t in range(T):
  W = stdin.readline().strip()
  D = deque(W[0])
  for w in W[1:]:
    if w >= D[0]:
      D.appendleft(w)
    else:
      D.append(w)
  print("Case #{}: {}".format(t + 1, "".join(D)))
    
  
