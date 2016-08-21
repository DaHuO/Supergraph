#!/bin/python
def run(x):
  if x == 0:
    return "INSOMNIA"
  d = dict()
  c = 0
  i = 0
  while True:
    i += 1
    n = x * i
    for s in str(n):
      if s not in d:
        d[s] = True
        c += 1
        if c >= 10:
          return n
    
  return "INSOMNIA"

t = input()
for i in range(1, t + 1):
  n = int(input())
  output = run(n)
  print "Case #{}: {}".format(i, output)

