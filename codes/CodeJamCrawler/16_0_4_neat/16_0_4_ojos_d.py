#!/usr/bin/env python

for nnn in xrange(1, int(raw_input())+1):
  print "Case #%d:" % (nnn),
  K, C, S = [int(x) for x in raw_input().split()]
  print ' '.join([str(x) for x in xrange(1, S+1)])
  #print 'IMPOSSIBLE'

