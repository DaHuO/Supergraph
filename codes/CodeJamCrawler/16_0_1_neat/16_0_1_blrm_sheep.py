#!/usr/bin/env python
# -*- coding: utf-8 -*-

def count_sheep(n):
  latest_num = int(n)
  if latest_num == 0:
    return "INSOMNIA"
  seen_digits = set([int(i) for i in str(latest_num)])
  while seen_digits != set(range(10)):
    latest_num += int(n)
    for i in str(latest_num):
      seen_digits.add(int(i))
  return latest_num


if __name__ == "__main__":
  testcases = input()
  for caseNr in xrange(1, testcases+1):
    starting_num = raw_input()
    print("Case #%i: %s" % (caseNr, count_sheep(starting_num)))
