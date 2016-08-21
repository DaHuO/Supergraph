#!/usr/bin/env python3
import sys

def digits(num):
  return list(str(num))

fin = open(sys.argv[1],'r')

T    = int(fin.readline())
nums = fin.readlines()
nums = list(map(int,nums))
for n in range(len(nums)):
  N = nums[n]
  s = set()
  for i in range(1,99999):
    s.update(digits(i*N))
    if len(s)==10:
      print("Case #{0}: {1}".format(n+1,i*N))
      break
  else:
    print("Case #{0}: INSOMNIA".format(n+1))