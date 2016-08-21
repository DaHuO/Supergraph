#!/usr/bin/python
from sys import stdin, stderr

def solve(num):
  if num == 0:
    return 'INSOMNIA'
  digits_not_seen = set()
  for i in range(10):
    digits_not_seen.add(i)
  i = 0
  while len(digits_not_seen):
    i += 1
    cur = num * i
    for digit in str(cur):
      try:
        digits_not_seen.remove(int(digit))
      except KeyError:
        pass
  return cur

num_cases = int(stdin.readline())
for case_num in range(num_cases):
  num = int(stdin.readline().strip())
  result = 'Case #{0}: {1}'.format(case_num + 1, solve(num))
  print result
  print >>stderr, result
