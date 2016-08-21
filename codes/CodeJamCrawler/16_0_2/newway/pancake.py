#! /usr/bin/env python
import sys,re

def min_flip(states, target):
  #states = shorten(states)
  #print("current:", states, "target:",target)
  if len(states) == 1:
    if target == '+':
      return 0 if states[0] == '+' else 1
    elif target == '-':
      return 0 if states[0] == '-' else 1

  elif states[-1] == '+' and target == '+':
    return min_flip(states[:-1], '+')

  elif states[-1] == '+' and target == '-':
    return min_flip(states[:-1], '+') + 1

  elif states[-1] == '-' and target == '+':
    return min_flip(states[:-1], '-')+1

  elif states[-1] == '-' and target == '-':
    return min_flip(states[:-1], '-')

with open (sys.argv[1]) as f:
  cases = int(f.readline())
  for case in range(cases):
    str1 = f.readline().strip()
    no_flip = min_flip(str1,'+')
    print("Case #%d: %s"%(case+1, no_flip))
#if len(test) == 1:
#  print (0 if test[0] == '+' else 1)
#else:


