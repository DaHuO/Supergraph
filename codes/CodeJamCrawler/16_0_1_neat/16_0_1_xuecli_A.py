#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
# to run
python A.py < A-small-practice.in > result.txt
'''

def solve(cipher):
  lst = [False] * 10
  count = 0
  cipher = int(cipher)

  if cipher == 0:
    return "INSOMNIA"

  N = 1

  while True:
    num = N * cipher
    while num != 0:
      digit = num % 10
      num = num / 10
      if not lst[digit]:
        lst[digit] = True
        count = count + 1
    if count == 10:
      return N * cipher   
    N = N + 1

if __name__ == "__main__":
  testcases = input()
   
  for caseNr in xrange(1, testcases+1):
    cipher = raw_input()
    print("Case #%i: %s" % (caseNr, solve(cipher)))