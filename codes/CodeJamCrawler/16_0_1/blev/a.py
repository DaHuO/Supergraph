

from sys import stdin
def readline(): return stdin.readline().strip('\n')
def readint(): return int(readline())

def getdigits(n):
   s = set()
   while n > 0:
     s.add(n % 10);
     n /= 10
   return s 

T = readint()

for t in range(1, T+1):
   N = readint()
   if N == 0:
      print 'Case #' + str(t) + ': INSOMNIA'
      continue
   digits = set()
   y = N
   i = 0
   while len(digits) < 10:
      i += 1
      y = i*N
      digits |= getdigits(y)
   print 'Case #' + str(t) + ': ' + str(y)

  
