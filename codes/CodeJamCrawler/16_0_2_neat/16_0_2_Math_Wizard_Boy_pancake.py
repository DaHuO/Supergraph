#!/bin/env python3
t = str.maketrans("+-", "01")

m = { 0 : 0 }
def a(n):
  if n not in m:
    if n % 4 == 0:
      m[n] = a(n // 2)
    elif n % 4 == 2:
      m[n] = 1 + a(n // 2)
    else:
      m[n] = 2 * a(n // 2) - a(n - 1) + 1
  return m[n]

def h(s):
  return a(int(str.translate(s, t)[::-1], 2))

l = int(input())

for i in range(l):
  s = input()
  print("Case #{}: {}".format(i + 1, h(s)))
