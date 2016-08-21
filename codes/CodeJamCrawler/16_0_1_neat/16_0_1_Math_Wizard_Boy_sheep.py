#!/bin/env python3
  
l = int(input())

for i in range(l):
  n = int(input())
  if n:
    left = set("0123456789")
    acc = 0
    while left:
      acc += n
      left -= set(str(acc))
    print("Case #{}: {}".format(i+1, acc))
  else:
    print("Case #{}: INSOMNIA".format(i + 1))
