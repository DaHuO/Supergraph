#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_number():
  return int(raw_input())

def solve(s):
  neg = pos = ans = 0
  for i, c in enumerate(s):
    if i == 0 or s[i] != s[i - 1]:
      if c == '-':
        ans = min(pos + 2, neg + 1)
        pos += 2
      else:
        ans = min(pos, neg + 1)
        neg += 2
  return ans

def main():
  T = get_number()
  for i in xrange(T):
    print 'Case #%d: %s' % (i + 1, solve(raw_input()))

if __name__ == '__main__':
  main()
