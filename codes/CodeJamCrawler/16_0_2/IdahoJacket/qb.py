import sys
import itertools

numCases = input()
for case in range( 1, numCases + 1 ):
  nOrig = raw_input()

  n = itertools.groupby( nOrig )
  groups = []
  for k, g in n:
    groups.append(list(g))      # Store group iterator as a list

  output = len(groups)
  if nOrig[-1] == '+':
    output -= 1

  print 'Case #' + str( case ) + ': ' + str( output )
