#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_number():
  return int(raw_input())

def solve(num):
  if num == 0:
    return 'INSOMNIA'
  digits = {}
  for i in xrange(1, 99999999):
    value = num * i
    for c in str(value):
      digits[c] = 0

    if len(digits) == 10:
      return value
  return 'INSOMNIA'

def main():
  T = get_number()
  for i in xrange(T):
    print 'Case #%d: %s' % (i + 1, solve(get_number()))

if __name__ == '__main__':
  main()