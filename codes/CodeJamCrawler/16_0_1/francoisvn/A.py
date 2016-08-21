#!/usr/bin/python

import sys

def all_hits(hits):
  for h in hits:
    if h == 0:
      return False
  return True

def update_hits(hits, n):
  if n == 0:
    hits[0] = 1
    return

  while n > 0:
    v = n % 10
    hits[v] = 1
    n = n / 10

T = int(sys.stdin.readline())
for test in range(T):
  print >> sys.stderr, "Test: %d" % (test+1)
  toks = sys.stdin.readline().strip().split()
  N = int(toks[0])
  
  hits = [0] * 10
  last = 0

  if N > 0:
    i = 1
    while not all_hits(hits):
      n = i * N;
      update_hits(hits,n);
      # print >> sys.stderr, i, n, hits
      last = n
      i += 1

  if all_hits(hits):
    print "Case #%d: %d" % (test+1, last)
  else:
    print "Case #%d: INSOMNIA" % (test+1)

