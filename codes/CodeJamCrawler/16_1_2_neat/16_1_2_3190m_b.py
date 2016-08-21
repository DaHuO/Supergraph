# -*- coding: utf-8 -*-

# Round 1A 2016
# Problem B. Rank and File

T = int(input())

for i in range(T):
  N = int(input())
  lines = [input().split(" ") for j in range(2 * N -1)]
  hs = []
  for k in range(2 * N - 1):
    hs = hs + lines[k]

  h = {}
  for m in hs:
    if m in h:
      h[m] += 1
    else:
      h[m] = 1

  a = []
  for k, v in h.items():
    if v % 2 != 0:
      a.append(int(k))

  ans = map(lambda x : str(x), sorted(a))

  print("Case #{}: {}".format(i + 1, " ".join(ans)))