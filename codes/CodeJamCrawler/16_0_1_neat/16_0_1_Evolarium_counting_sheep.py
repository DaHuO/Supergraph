#!/usr/bin/env pypy

import sys,os
from collections import defaultdict

def digits(n, d):
  while True:
    digit = n%10
    d.add(digit)
    n /= 10
    if(n<=0):
      break

with open(sys.argv[1]) as f:
  num_entries = int(f.readline().strip())
  for i in range(0,num_entries):
    N = int(f.readline().strip())
    d = set()
    nN = N
    idx = 1

    if N == 0:
      sys.stdout.write("Case #{}: INSOMNIA\n".format(i+1))
      continue

    while len(d) != 10:
      digits(nN, d)
      idx += 1
      nN = idx*N
    sys.stdout.write("Case #{}: {}\n".format(i+1, (idx-1)*N))
