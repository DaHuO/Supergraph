#!/usr/bin/env python3
# encoding: utf-8

import sys
from pprint import pprint

def solveCase(s):
  r = s[0]
  for c in s[1:]:
    if (c + r) > (r + c):
      r = (c + r)
    else:
      r = (r + c)
  
  return r

def solve(s):
  t = int(s.readline())
  
  for i in range(t):
    l = s.readline().strip()
  
    yield solveCase(l)

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