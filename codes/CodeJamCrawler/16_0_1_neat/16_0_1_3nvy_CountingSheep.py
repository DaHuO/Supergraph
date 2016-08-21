#!/usr/bin/env python
"""Google Code Jam 2016: Problem A. Counting Sheep"""

from builtins import input


def main():
  T = int(input())
  if T < 1 or T > 100:
    raise RuntimeError("T is not within the valid range")
  for i in range(T):
     N = int(input())
     if N < 0 or N > 1000000:
       raise RuntimeError("N is not within the valid range")
     r = fallAsleep(N)
     print("Case #" + str(i + 1) + ": " + r)
    


def fallAsleep(N):
  if N == 0:
    return "INSOMNIA"
  s = set()
  i = 0

  while len(s) != 10:
    i += 1
    s |= set(str(i * N))
    if i > 10000:
      return "INSOMNIA"
  return str(i * N)
    
    

if __name__=="__main__":
  main()
