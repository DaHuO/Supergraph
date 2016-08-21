#!/usr/bin/env python

import sys
import math
import copy

cases = int(sys.stdin.readline().strip())

def paths_in_graph(matrix):

  actives = [0]

  n_paths = 0
  dst = len(matrix)-1
  while len(actives) > 0:
    src = actives.pop()
    if src == dst:
      n_paths += 1
    else:
      for i in xrange(len(matrix[src])):
        if matrix[src][i] != 0:
          actives.append(i)

  return n_paths

for c in xrange(cases):
  N, M = map(int, sys.stdin.readline().split())

  matrix = []
  for i in xrange(N-1):
    matrix.append([0]*(i+1)+[1]*(N-i-1))
  matrix.append([0]*N)

  max_paths = paths_in_graph(matrix)

  if max_paths < M:
    print "Case #%d: IMPOSSIBLE" %(c+1)
  else:
    #delete paths
    actives = [(0 , matrix)]
    while len(actives) > 0:
      ini, m = actives.pop()
      if paths_in_graph(m) == M:
        print "Case #%d: POSSIBLE" %(c+1)
        for i in m:
          print "".join([str(x) for x in i])
        break

      for src in xrange(ini, len(m)):
        if sum(m[src]) == 0:
          continue
        for dst in xrange(src, len(m)):
          if m[src][dst] == 1:
            m_new = []
            for i in m:
              m_new.append([x for x in i])
            m_new[src][dst] = 0
            actives.append((src+1, m_new))
    
