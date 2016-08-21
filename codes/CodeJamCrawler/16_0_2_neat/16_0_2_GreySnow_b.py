#!/usr/bin/env python3
import sys

def ProcLine(s):
  s       = s[::-1]
  flips   = 0
  flipped = False
  for i in s:
    if flipped:
      if i=='-':
        continue
      else:
        flipped = not flipped
        flips  += 1
    else:
      if i=='+':
        continue
      else:
        flipped = not flipped
        flips  += 1
  return flips

fin = open(sys.argv[1],'r')

T    = int(fin.readline())
nums = fin.readlines()
nums = list(map(lambda x: x.strip(),nums))

for n in range(len(nums)):
  flips = ProcLine(nums[n])
  print("Case #{0}: {1}".format(n+1,flips))