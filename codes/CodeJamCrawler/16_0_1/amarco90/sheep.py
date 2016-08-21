#!/usr/bin/env python3

import sys

def add_digits(n, digits):
  s = str(n)
  for c in s:
    digits[c] = digits.get(c, 0) + 1

def all_digits(digits):
  return all(digits.get(chr(x), 0) > 0 for x in range(48, 58))

if __name__ == '__main__':
  T = int(sys.stdin.readline())

  for t in range(1, T+1):
    N = int(sys.stdin.readline())

    digits = {}
    i = 1
    current = i * N
    add_digits(current, digits)
    while not all_digits(digits):
      i += 1
      current = i * N
      if current == N: break;
      add_digits(current, digits)

    print('Case #{}: {}'.format(t, current if current != N else 'INSOMNIA'))
