#!/usr/bin/env python3
# encoding: utf-8

import sys
from pprint import pprint

def solveCase(n, lines):
  count = {}
  for line in lines:
    for i in line:
      count[i] = count.get(i, 0) + 1
  
  result = []
  for i in count:
    if count[i] % 2 == 1:
      result.append(i)
  
  result.sort()
  return result

def solve(s):
  t = int(s.readline())
  
  for i in range(t):
    n = int(s.readline())
    lines = []
    for j in range(2 * n - 1):
      lines.append([int(x) for x in s.readline().split()])
    yield ' '.join(str(x) for x in solveCase(n, lines))

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