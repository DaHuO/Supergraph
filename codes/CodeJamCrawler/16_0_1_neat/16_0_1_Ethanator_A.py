#!/usr/bin/python -tt

def count(m):
  if m == 0:
    return "INSOMNIA"
  a = [False, False, False, False, False, False, False, False, False, False]
  filled = 10
  mmm = m
  while filled > 0 and m < 10**100:
    mm = m
    while mm > 10:
      last_dig = mm % 10
      if not a[last_dig]:
        a[last_dig] = True
        filled -= 1
      mm = mm / 10
    if mm == 10:
      if not a[0]:
        a[0] = True
        filled -= 1
      if not a[1]:
        a[1] = True
        filled -= 1
    elif not a[mm]:
      a[mm] = True
      filled -= 1
    if filled == 0:
      break
    m += mmm
  return m

n = int(raw_input())
for i in xrange(n):
  x = int(raw_input())
  print "Case #" + str(i+1) + ": " + str(count(x))
