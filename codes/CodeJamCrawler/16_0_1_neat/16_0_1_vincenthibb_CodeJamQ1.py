import sys



def solve(N):
   ANS = [0,1,2,3,4,5,6,7,8,9]
   ANSset = set(ANS)
   for Trial in range(1,3000):
       Number = N*Trial
       NumberList = [int(i) for i in str(Number)]
       NumberListSet = set(NumberList)
       ANSset = ANSset - NumberListSet
       if not ANSset:
           return str(N*(Trial))
           break
       elif Number == N*(Trial+1):
           return "INSOMNIA"
           break



numcases = int(sys.stdin.readline())
N = [None] * numcases
for casenum in range(0,numcases):
   N[casenum] = int(sys.stdin.readline())

for casenum in range(0,numcases):
   print 'Case #' + repr(casenum+1) + ': ' + solve(N[casenum])



