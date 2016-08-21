#!/usr/bin/python

import operator
import sys
import random

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

# number -> party

def solve(senators):
  evacs = []
  tups = senators.items()
  while True:
    tups = sorted(tups, key=operator.itemgetter(1), reverse=True)
    #print tups
    if tups[0][1] is 0 and tups[1][1] is 0:
      return evacs

    m1 = tups[0]
    m2 = tups[1]

    if m1[1] is 1 and m2[1] is 1:
      if len(tups) > 2 and tups[2][1] > 0: # 1 1 1 ....
        evacs.append('' + m1[0])
        tups[0] = (m1[0], m1[1] - 1)
      else: # 1 1 0 ...
        evacs.append('' + m1[0] + m2[0])
        tups[0] = (m1[0], m1[1] - 1)
        tups[1] = (m2[0], m2[1] - 1)
    elif m1[1] - m2[1] is 0: # x x ...
      evacs.append('' + m1[0] + m2[0])
      tups[0] = (m1[0], m1[1] - 1)
      tups[1] = (m2[0], m2[1] - 1)
    else: # 4 2 ...
      evacs.append('' + m1[0])
      tups[0] = (m1[0], m1[1] - 1)
    # check if all 0

if False:
  print 50
  for i in xrange(50):
    s = random.randint(2, 26)
    print s
    nums = []
    for j in xrange(s):
      nums.append(str(random.randint(1, 1000)))
    print ' '.join(nums)
  sys.exit()

lines = iter(sys.stdin.readlines())
cases = int(lines.next())
for i in xrange(cases):
  senators = {}
  s = int(lines.next())
  numbers = [int(num) for num in lines.next().split(' ')]
  for j in xrange(s):
    senators[ALPHA[j]] = numbers[j]
  print "Case #%d: %s" % (i + 1, ' '.join(solve(senators)))



