#!/usr/bin/python

import sys

def solve(pancakes):
  transitions = 0
  prev = None
  for p in pancakes:
    if prev and p != prev:
      transitions += 1
    prev = p
  if p == '-':
    return transitions + 1
  else:
    return transitions

lines = iter(sys.stdin.readlines())
cases = int(lines.next())
for i in xrange(cases):
  pancakes = lines.next().strip()
  print "Case #%d: %d" % (i + 1, solve(pancakes))


'''
Reasoning

-+ => ok, just 1
+-  > --  > ++ => 2

so maybe it sucks to have negs after pluses. we'll have to flip them at some point.

++-- => 2

++++++++++++++-------------- => 2

does it ever make sense to flip in the middle of a section? i really doubt it.
which means we can simplify the problem to single +/-'s.

hunch: count the transitions. add 1 if it starts with +. (or if it ends with -?)

solution:
-+-+-+-+- (8 transitions, ends in -. expect 9 moves)
++-+-+-+- 1
---+-+-+- 2
++++-+-+- 3
-----+-+- 4
++++++-+- 5
-------+- 6
++++++++- 7
--------- 8
+++++++++ 9


--++--

+++----++++-++--++
'''
