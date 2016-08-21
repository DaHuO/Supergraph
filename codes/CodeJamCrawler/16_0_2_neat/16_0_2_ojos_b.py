#!/usr/bin/env python

for nnn in xrange(1, int(raw_input())+1):
  print "Case #%d:" % (nnn),
  S = raw_input().strip()
  num_flips = 0
  for i in xrange(len(S)-1):
    if S[i] != S[i+1]:
      num_flips += 1
  if S[-1] == '-':
    num_flips += 1
  print num_flips

