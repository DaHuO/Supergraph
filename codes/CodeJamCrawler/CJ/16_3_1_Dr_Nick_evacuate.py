#!/usr/bin/env python

import sys

def add_evacs(sol, senators):
  if len(senators) == 1:
    senators[0] -= 1
    return [ ("%s" %(chr(senators[0] + ord('A'))), senators) ]

  res = []
  s = sum(senators)

  v = [ (senators[i], i) for i in xrange(len(senators)) ]
  v.sort()
 
  if senators[v[-2][1]] <= (s-2) / 2:
    senator_1 = chr(v[-1][1] + ord('A'))
    new_senators = [ x for x in senators ]
    new_senators[v[-1][1]] -= 2
    new_sol = sol + [ "%s%s" %(senator_1, senator_1) ]
    res.append((new_sol, new_senators))

  if senators[v[-2][1]] <= (s-1) / 2:
    senator_1 = chr(v[-1][1] + ord('A'))
    new_senators = [ x for x in senators ]
    new_senators[v[-1][1]] -= 1
    new_sol = sol + [ "%s" %(senator_1) ]
    res.append((new_sol, new_senators))

  senator_1 = chr(v[-1][1] + ord('A'))
  senator_2 = chr(v[-2][1] + ord('A'))
  new_senators = [ x for x in senators ]
  new_senators[v[-1][1]] -= 1
  new_senators[v[-2][1]] -= 1
  new_sol = sol + [ "%s%s" %(senator_1, senator_2) ]
  res.append((new_sol, new_senators))

  return res
      

cases = int(sys.stdin.readline().strip())

for c in xrange(cases):
  n_senators = int(sys.stdin.readline().strip())
  senators = map(int, sys.stdin.readline().split())[0:n_senators]

  actives = add_evacs([], senators)

  while True:
    current_sol, current_senators = actives.pop()

    s = sum(current_senators)

    if s == 0:
      print "Case #%d: %s" %(c+1, " ".join(current_sol))
      break
    elif s > 1:
      actives += add_evacs(current_sol, current_senators)

