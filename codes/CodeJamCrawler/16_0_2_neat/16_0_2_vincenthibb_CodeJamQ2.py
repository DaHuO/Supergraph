import sys


def solve(b):
 b = [str(i) for i in str(b)]
 FlipTime = 0
 posnum = 0
 for Trial in range(1,30000):
  b = NoendPositive(b)
  if not b:
    return FlipTime
    break
  if b[0] == '+':
    for i in range(0,len(b)):
       if b[i] != "+":
          posnum = i
          break
    b,FlipTime = flip(b,posnum,FlipTime)
  elif b[0] == '-':
   b,FlipTime = flip(b,len(b),FlipTime)

  b = NoendPositive(b)
  if not b:
    return FlipTime
    break

def flip(P,End,FlipTime):
     FlipTime = FlipTime + 1
     P[0:End] = P[0:End][::-1]
     for i in range(0,End):
        if P[i] == "+":
           P[i] = "-"
        elif P[i] == "-":
            P[i] = "+"
     return P,FlipTime

def NoendPositive(P):
    length = len(P)
    TempP = []
    for i in range(length-1,-1,-1):
      if P[i] == '+':
          TempP = P[0:i]
      else:
          if not TempP:
              TempP = P
          break
    return TempP

numcases = int(sys.stdin.readline())
board = []
for casenum in range(0,numcases):
   board.append(sys.stdin.readline().strip())

for casenum in range(0,numcases):
    print 'Case #' + repr(casenum+1) + ': ' + str(solve(board[casenum]))
