#!/usr/bin/env python

for nnn in xrange(1, int(raw_input())+1):
  print "Case #%d:" % (nnn),
  N = int(raw_input())
  if N == 0:
    print 'INSOMNIA'
  else:
    last = N
    seen = [0] * 10
    while True:
      tmp = last
      while tmp > 0:
        seen[tmp%10] = 1
        tmp /= 10
      if sum(seen) == 10:
        print last
        break
      last += N

