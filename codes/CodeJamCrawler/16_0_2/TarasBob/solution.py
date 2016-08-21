#!/usr/bin/python
from sys import stdin, stderr

def solve(cakes):
  num_transitions = 0
  prev_cake = cakes[0]
  for cake in cakes:
    if cake != prev_cake:
      num_transitions += 1
      prev_cake = cake
  if cakes[-1] == '-':
    num_transitions += 1
  return num_transitions

num_cases = int(stdin.readline())
for case_num in range(num_cases):
  cakes = stdin.readline().strip()
  result = 'Case #{0}: {1}'.format(case_num + 1, solve(cakes))
  print result
  print >>stderr, result
