from sys import stdin
from itertools import combinations

T = int(stdin.readline())

def P2(Q, p):
  return [a + b for (a,b) in zip([q * (1 - p) for q in Q] + [0], [0] + [q * p for q in Q])]

for t in range(T):
  N, K = (int(i) for i in stdin.readline().split())
  P = [float(i) for i in stdin.readline().split()]
  B = 0.0
  for p in combinations(P, K):
    Q = [1]
    for q in p:
      Q = P2(Q, q)
    b = Q[len(Q) / 2]
    if b > B:
      B = b
  print('Case #{}: {}'.format(t + 1, B))
