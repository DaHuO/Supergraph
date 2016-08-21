import sys
from decimal import *

s=sys.stdin.read().split('\n')

for k in range( int(s[0]) ):
  #print( s[k+1] )

  start = Decimal( s[k+1] )
  if start == 0:
    print('Case #' + str(k+1) + ': INSOMNIA')
    continue
  mul=0
  ara=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
  #print( ara )
  while sum(ara)<10:
    mul+=1
    for l in str(start*mul):
      ara[ord(l)-ord('0')]=1
    #print(ara)
  print( 'Case #' + str(k+1) + ': ' + str(start*mul) )
