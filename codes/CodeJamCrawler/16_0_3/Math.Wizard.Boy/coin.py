#!/bin/env python3
from sys import stdin

t = int(stdin.readline())

def f(n):
  if n % 2 == 0:
    return 2
  if n % 3 == 0:
    return 3
  i = 5 
  d = 2
  while i <= 37:
    if n % i == 0:
      return i
    i += d
    d = 6 - d
  return None

for i in range(t):
  n, j = (int(x) for x in stdin.readline().split())
  x = 2 ** (n - 1) + 1
  print("Case #{}:".format(i + 1))
  while j:
    s = format(x, 'b')
    fs = [f(int(s,i)) for i in range(2,11)]
    if all(fs):
      print(s, " ".join(str(f) for f in fs))
      j -= 1
    x += 2
      
    
    
  


