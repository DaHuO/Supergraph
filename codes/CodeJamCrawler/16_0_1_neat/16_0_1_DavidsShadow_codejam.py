#!/usr/bin/python2.7
# codejam.py

from collections import Counter

T = int(raw_input())

def sleepy_time(n):
  if n:
    bag = Counter("")
    for i in xrange(1,10**6):
      bag.update(str(n*i))
      if len(bag) == 10:
        return str(n*i)
  
  return "INSOMNIA"

for case_nbr in xrange(1, T+1):
  solution = sleepy_time(int(raw_input()))
  print "Case #{}: {}".format(case_nbr, solution)
