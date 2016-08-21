#!/usr/bin/env python3
# encoding: utf-8

import sys
from pprint import pprint

def solveCase(n):
  if n == 0:
    return "INSOMNIA"

  nums = set(range(0,10))
  i = 1
  while True:
    k = i * n
    for c in str(k):
      if (int(c)) in nums:
        nums.remove(int(c))
    #print(k, list(nums))
    if (len(nums) == 0):
      break
    i += 1

  return k

def solve(s):
  t = int(s.readline())
  
  for i in range(t):
    yield solveCase(int(s.readline()))

def main(argv=None):
  fileName = argv[1]
  s = open(fileName)
  r = open(fileName + '.result.txt'  , 'w')

  result = solve(s)
  for i, case in enumerate(result, 1):
    r.write('Case #' + str(i) + ': ' + str(case) + '\n')
        
  return 0

if __name__ == '__main__':
  status = main(sys.argv)
  sys.exit(status)