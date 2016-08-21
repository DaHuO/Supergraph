#!/usr/bin/python
import random
from sys import stdin, stderr

def construct_number(N):
  prefix = '1'
  middle = ''.join(random.choice(['1', '0']) for _ in range(N-2))
  suffix = '1'
  return prefix + middle + suffix

def get_number_in_base(num, base):
  total = 0
  for i, digit in enumerate(reversed(num)):
    total += int(digit) * (base ** i)
  return total

def find_divisor(num):
  MAX_DIV = 1000
  for i in xrange(3, MAX_DIV):
    if num % i == 0:
      return i

def solve(N, J):
  num_found = 0
  results = {}
  while num_found < J:
    candidate = construct_number(N)
    if candidate in results:
      continue
    divisors = []
    for base in xrange(2, 11):
      num_b = get_number_in_base(candidate, base)
      divisor = find_divisor(num_b)
      if divisor is None:
        break
      else:
        divisors.append(divisor)
    else:
      results[candidate] = divisors
      num_found += 1
  ret_val = 'Case #1:'
  for cand in results:
    ret_val += '\n' + cand + ' ' + ' '.join(str(x) for x in results[cand])
  return ret_val

num_cases = int(stdin.readline())
for case_num in range(num_cases):
  N, J = [int(x) for x in stdin.readline().strip().split()]
  result = solve(N, J)
  print result
