#!/usr/bin/python

for c in xrange(int(raw_input())):
  p = '.'
  f = 0
  for x in raw_input():
    if x != p:
      f += 1
      p = x
  if x == '+':
    f -= 1
  print 'Case #%d: %d' % (c + 1, f)

