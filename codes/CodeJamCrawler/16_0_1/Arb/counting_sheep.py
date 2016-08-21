#!/usr/bin/env python

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer

for case in xrange(1, t + 1):
  n = int(raw_input())
  as_set = set(str(n))
  if n == 0:
    print "Case #{}: {}".format(case, 'INSOMNIA')
    continue
  elif len(as_set) == 10:
    print "Case #{}: {}".format(case, n)
    continue

  for i in xrange(2, 100):
    as_set.update(set(str(n * i)))
    if len(as_set) == 10:
      print "Case #{}: {}".format(case, n * i)
      break
  # check out .format's specification for more formatting options
