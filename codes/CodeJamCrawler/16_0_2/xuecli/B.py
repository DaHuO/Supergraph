#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque

def solve(pancakes):
  length = len(pancakes)
  stack = [0] * length
  for i in range(length):
    if pancakes[i] == '-':
      stack[i] = 0
    else:
      stack[i] = 1
  stack = tuple(stack)
  step = 0
  queue = deque()
  seen = {}

  queue.append(stack)
  seen[stack] = 0
  queue.append("")
  # BFS
  while True:
    stack = queue.popleft()
    if stack == "":
      step = step+1
      queue.append("")
    elif sum(stack) == length:
      return step
    else:
      for i in range(length):
        new_stack = flip(stack, i)
        if not seen.has_key(new_stack):
          seen[new_stack] = 0
          queue.append(new_stack)
  return step

def flip(stack, idx):
  new_stack = [0] * len(stack)
  for i in range(idx+1):
    new_stack[i] = 1 - stack[idx-i]
  for i in range(idx+1, len(stack)):
    new_stack[i] = stack[i]
  return tuple(new_stack)

if __name__ == "__main__":
  testcases = input()
   
  for caseNr in xrange(1, testcases+1):
    cipher = raw_input()
    print("Case #%i: %s" % (caseNr, solve(cipher)))