#!/usr/bin/python
import sys

inputs = [line.strip() for line in sys.stdin]

T = int(inputs[0])

for t in xrange(T):
  S = inputs[t+1] + "+"
  count = 0
  for i in xrange(len(S)-1):
    if S[i] != S[i+1]:
      count += 1
  print "Case #{0}: {1}".format(t+1, count)

