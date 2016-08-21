import sys

IT = 0
MAX = 1

PARTY = 0
COUNT = 1

A_CODE = 65

def party_comparer(a, b): return b[COUNT] - a[COUNT]

def kick_max(P, it, max):
  curr = P[it]
  if curr[COUNT] != max:
    it += 1
    if it < len(P) and P[it][COUNT] == max:
      curr = P[it]
    else:
      it = 0
      curr = P[it]
      max = curr[COUNT]

  sys.stdout.write(curr[PARTY])
  curr[COUNT] -= 1
  if curr[COUNT] == 0: P.pop(it)
  else: it += 1
  if it == len(P) and len(P) > 0:
    it = 0
    max = P[it][COUNT]
  return [it, max]

def total(P):
  sum = 0
  for i in range(len(P)): sum += P[i][COUNT]
  return sum

T = int(raw_input())
for t in range(T):
  N = int(raw_input())
  P = map(int, raw_input().split())
  for j in range(N): P[j] = [chr(A_CODE + j), P[j]]
  P.sort(party_comparer)
  sys.stdout.write("Case #" + str(t + 1) + ":")
  it = 0
  max = P[it][COUNT]
  first_skip = (total(P) % 2 == 1)
  while len(P) > 0:
    sys.stdout.write(" ")
    if not first_skip:
      it, max = kick_max(P, it, max)
    first_skip = False
    it, max = kick_max(P, it, max)
  sys.stdout.write("\n")
