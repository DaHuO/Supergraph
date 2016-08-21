#!/usr/bin/python
import sys

inputs = [int(line.strip()) for line in sys.stdin]

T = inputs[0]

for t in xrange(T):
  N = inputs[t+1]
  if (N == 0):
    print("Case #{0}: INSOMNIA".format(t+1))
  else:
    seen = set(str(N))
    k = N
    while (len(seen) != 10):
      k += N
      seen = seen | set(str(k))
    print("Case #{0}: {1}".format(t+1, k))
