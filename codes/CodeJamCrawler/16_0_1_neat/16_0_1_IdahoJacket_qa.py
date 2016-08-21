import sys

numCases = input()
for case in range( 1, numCases + 1 ):
  nOrig = input()
  seen = set()

  n = 0
  if nOrig > 0:
    while len(seen) < 10:
      n = n + nOrig
      nStr = str(n)
      for a in nStr:
        seen.add(int(a))

  output = n
  if output == 0:
    output = "INSOMNIA"

  print 'Case #' + str( case ) + ': ' + str( output )
