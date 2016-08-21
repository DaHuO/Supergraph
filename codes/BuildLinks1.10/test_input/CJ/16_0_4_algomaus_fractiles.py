#! /usr/bin/env python

def solve(line):
  line_splitted = line.split(' ')
  K = int(line_splitted[0])
  C = int(line_splitted[1])
  S = int(line_splitted[2])
  
  if S >= K:
    res = ""
    for i in range(K-1):
      res = res + str(i+1) + ' '
    res = res + str(K)
    return res
  else:
    # try very naive approach and hope for small inputs
    
    pass # TODO
      
  return "IMPOSSIBLE"
    
with open('D-small-attempt0.in', 'r') as f:
#with open('input', 'r') as f:
  lines = f.read().splitlines()
for i in range(len(lines)-1):
  sol = solve(lines[i+1])
  print "Case #" + str(i+1) + ": " + str(sol)
