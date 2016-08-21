#!/usr/bin/env python3
# encoding: utf-8

import sys
from pprint import pprint

def solveCase(s):
  prev = s[0]
  res = 0
  for c in s:
    if c != prev:
      res += 1
    prev = c
      
  if (res % 2 == 1):
    if s[0] == '+':
      return res + 1 
    else:
      return res
  else: 
    if s[0] == '-':
      return res + 1 
    else:
      return res

  

def solve(s):
  t = int(s.readline())
  
  for i in range(t):
    yield solveCase(s.readline().strip())

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