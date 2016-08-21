#!/usr/bin/env python
# -*- coding: utf-8 -*-

# All numbers are actually strings

def empty_hash():
  h = {}

  for i in range(10):
    h[str(i)] = False

  return h

def is_complete(a_hash):
  for n in a_hash.values():
    if not n:
      return False

  return True

def solve(number):
  seen = empty_hash()

  multiplier = 1

  while True:
    current_number = str(int(number) * multiplier)

    for ch in current_number:
      seen[ch] = True

    if is_complete(seen):
      break
    else:
      multiplier += 1

  return current_number

test_cases = raw_input()

for case in range(1, int(test_cases) + 1):
  number = raw_input()
  if number == '0':
    print "Case #%s: %s" % (str(case), 'INSOMNIA')
  else:
    print "Case #%s: %s" % (str(case), solve(number))
