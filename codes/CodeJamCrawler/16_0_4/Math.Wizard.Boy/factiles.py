#!/bin/env python3
from sys import stdin

def l(n, k, c):
  return sum((n + i) * k ** (c - i - 1)  for i in range(c)) + 1

def g(k, c):
  return [l(c * i, k, c) for i in range(k // c)]

t = int(stdin.readline())
for i in range(t):
  k, c, s = (int(x) for x in stdin.readline().split())
  if c > k:
    c = k
  r = g(k, c)
  if k % c:
    r.append(k ** c - r[0] + 1)
  if len(r) > s:
    print("Case #{}: IMPOSSIBLE".format(i + 1))
  else:
    print("Case #{}: {}".format(i + 1, " ".join(str(x) for x in r)))
