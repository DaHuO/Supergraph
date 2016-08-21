#!/usr/bin/env python

for nnn in xrange(1, int(raw_input())+1):
  print "Case #%d:" % (nnn),
  N = int(raw_input())
  lines = [0] * (2*N-1)
  for nn in xrange(2*N-1):
    lines[nn] = [int(x) for x in raw_input().split()]

  arranged = [0] * (2*N)
  deleted = [False] * (2*N-1)
  maximum = 2501
  for i in xrange(N):
    minimum = maximum
    for j in xrange(2*N-1):
      if not deleted[j]:
        if lines[j][i] < minimum:
          minimum = lines[j][i]
          found = [j, -1]
        elif lines[j][i] == minimum:
          found[1] = j
    arranged[2*i] = lines[found[0]]
    deleted[found[0]] = True
    if found[1] == -1:
      missing = i
    else:
      arranged[2*i+1] = lines[found[1]]
      deleted[found[1]] = True

  ans = [0]*N
  other = arranged[2*missing]
  for i in xrange(N):
    if i != missing:
      if other[i] == arranged[2*i][missing]:
        ans[i] = arranged[2*i+1][missing]
      else:
        ans[i] = arranged[2*i][missing]
  ans[missing] = other[missing]

  print ' '.join([str(x) for x in ans])

