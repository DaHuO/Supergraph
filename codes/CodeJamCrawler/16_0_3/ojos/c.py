#!/usr/bin/env python

from math import sqrt

POWERS = []

def convert_from_binary(num, base):
  global POWERS
  if base == 2:
    return num
  else:
    binary_form = bin(num)[2:]
    N = len(binary_form)
    return sum([int(binary_form[N-i-1]) * POWERS[base][i] for i in xrange(N)])

def find_factor(x):
  for i in xrange(3, min(10001, int(sqrt(x))+1)):
    if x % i == 0:
      return i
  return None

for nnn in xrange(1, int(raw_input())+1):
  print "Case #%d:" % (nnn)
  N, J = [int(x) for x in raw_input().split()]
  POWERS = [[0] * N for i in xrange(11)]
  for i in xrange(3, 11):
    POWERS[i][0] = 1
    for j in xrange(1, N):
      POWERS[i][j] = POWERS[i][j-1] * i

  for num in xrange(2**(N-1)+1, 2**N, 2):
    # 2..10 = 9 elements
    factors = [0]*9
    failed = False
    for i in xrange(9):
      x = convert_from_binary(num, i+2)
      factors[i] = find_factor(x)
      if factors[i] is None:
        failed = True
        break
    if not failed:
      print bin(num)[2:], ' '.join([str(x) for x in factors])
      J -= 1
    if J == 0:
      break

