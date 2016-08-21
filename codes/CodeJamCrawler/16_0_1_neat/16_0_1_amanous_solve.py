#!/usr/bin/env python

T = int(raw_input())

def read_problem():
  n = int(raw_input())
  return n

def solve(problem):
  n = problem
  if n == 0:
    return 'INSOMNIA'
  s = set([str(i) for i in range(10)])
  i = 0
  while s:
    i += 1
    t = str(n * i)
    #print i, t
    for c in t:
      try:
        s.remove(c)
        #print 'removed', c
      except KeyError, e:
        pass
  return t

for n in range(T):
  problem = read_problem()
  solution = solve(problem)
  print 'Case #%d: %s' %(n+1, solution)

