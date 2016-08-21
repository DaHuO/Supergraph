from sys import stdin
from collections import defaultdict

T = int(stdin.readline())

def C(i, cI):
  cM = 0
  for j in cI[i]:
    cm = C(j, cI)
    if cm > cM:
      cM = cm
  # print("{} has chain length {}".format(i, cM + 1))
  return cM + 1

for t in range(T):
  N = int(stdin.readline())
  ML = 0
  MP = 0
  F = [int(i) - 1 for i in stdin.readline().split()]
  
  # Calculate the longest loop
  S = set()
  for n in range(N):
    L = {}
    k = 0
    while n not in L and n not in S:
      L[n] = k
      S.add(n)
      n = F[n]
      k += 1
    if n in L:
      m = k - L[n]
      if m > ML:
        ML = m
  
  I = defaultdict(set)
  for i,f in enumerate(F):
    if i != F[f]:
      I[f].add(i)
  # print(I)
  
  for i in range(N):
    if i == F[F[i]]:
      # print("Found pair {}, {}".format(i, F[i]))
      MP += C(i, I)
  print("Case #{}: {}".format(t + 1, max(ML, MP)))
