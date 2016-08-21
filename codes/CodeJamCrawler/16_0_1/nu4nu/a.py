#!/usr/bin/python

for c in xrange(int(raw_input())):
  n = int(raw_input())
  if not n:
    print 'Case #%d: INSOMNIA' % (c + 1)
    continue
  x = n
  v = set(str(d) for d in xrange(0, 10))
  while True:
    v -= set(str(x))
    if not v:
      break
    x += n
  print 'Case #%d: %d' % (c + 1, x)

