import sys

numCases = input()
for case in range( 1, numCases + 1 ):
  (k,c,s) = [int(x) for x in raw_input().split()]

  sectionSize = (k)**(c-1)
  output = ""

  for i in xrange(0,k):
    tile = 1
    offset = 0
    for j in xrange(0,c):
      offset += k**j
    tile += i * offset
    output += " " + str(tile)

  output = output

  print 'Case #' + str( case ) + ': ' + str( output )
