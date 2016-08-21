#!/usr/bin/env python3

import sys

def main():
  fi = sys.stdin
  fo = sys.stdout
  caseCount = int(fi.readline().strip())
  for i in range(1, caseCount+1):
    n = readInput(fi)
    solution = solve(n)
    displayAndClear(fo, i, solution)

def readInput(f):
  return int(f.readline().strip())

def displayAndClear(f, i, solution):
  if solution == -1:
    f.write('Case #%d: INSOMNIA\n' % i)
  else:
    f.write('Case #%d: %d\n' % (i, solution))
  f.flush()

def solve(n):
  if n == 0:
    return -1

  unseen = set(range(10))
  coeff = 1
  cur_num = -1
  while unseen:
    cur_num = coeff * n
    update_unseen(unseen, cur_num)
    coeff += 1

  return cur_num

def update_unseen(unseen, num):
  while num > 0:
    cur_digit = num % 10
    unseen.discard(cur_digit)
    num //= 10

if __name__ == '__main__':
  main()

