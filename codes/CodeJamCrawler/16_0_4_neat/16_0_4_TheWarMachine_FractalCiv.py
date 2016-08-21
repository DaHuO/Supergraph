import math

T = int(raw_input())
for tt in range(1,T+1):
  K,C,S = map(int,raw_input().split())
  KPowC = K**(C-1)
  totalLen = K**(C+1)
  outputString = ['Case #%d: ' % tt]
  curPos = 1L
  for s in range(S):
    outputString.append('%d ' % curPos)
    curPos += (KPowC)
  print ''.join(outputString)
