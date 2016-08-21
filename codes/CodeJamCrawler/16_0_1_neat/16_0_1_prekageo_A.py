#!/usr/bin/env python

import sys

def rl():
  return sys.stdin.readline().strip()

def solve_one():
  n = int(rl())
  seen = set()
  count = 1
  while True:
    new = seen.union(set(list(str(count * n))))
    if count > 1000000:
      return 'INSOMNIA'
    seen = new
    if len(seen) == 10:
      return str(count * n)
    count += 1

def main():
  for i in xrange(int(rl())):
    print 'Case #%d: %s' % (i+1,solve_one())

if __name__ == '__main__':
  main()
