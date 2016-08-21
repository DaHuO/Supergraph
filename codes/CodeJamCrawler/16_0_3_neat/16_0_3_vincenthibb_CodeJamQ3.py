import sys
import itertools as it
import math
import random
from collections import Counter
WorkPermutationList = []
Smallestdivisors = []
checker = True
Time = 0
arraylist = []
ans = []

numcases = int(sys.stdin.readline())
the_string = raw_input()
N, J = the_string.split()
N = int(N)
J = int(J)
print 'Case #' + str(1)+ ': '

for Trial in xrange(0,3000000):
            arraylist = []
            for i in xrange(0,N-2):
              a = int(round(random.random()))
              arraylist.append(a)

            Valuelist = [0]*9
            Smallestdivisorssub = []

            TotalArrayList = [1]+list(arraylist)+[1]
            Testing = TotalArrayList[::-1]

            for primetest in xrange(2,11):

                for size in xrange(0,N):

                   Valuelist[primetest-2] = Valuelist[primetest-2] + Testing[size] * int(math.pow(primetest,size))

            for Value in xrange(0,9):

               for primecheck in xrange(2,Valuelist[Value]):

                    checker = False

                    if Valuelist[Value] % primecheck == 0:
                      checker = True
                      Smallestdivisorssub.append(primecheck)
                      break

                    elif primecheck > 1000000:
                      checker = False
                      Smallestdivisorssub = []
                      break

               if checker == False:
                  break


            if checker ==  True:
                 if TotalArrayList in ans:
                      continue
                 ans.append(TotalArrayList)
                 Time = Time + 1
                 WorkPermutationList.append(TotalArrayList)
                 Smallestdivisors.append(Smallestdivisorssub)
                 ds = "".join([str(x) for x in WorkPermutationList[0]])
                 dt = " ".join([str(x) for x in Smallestdivisors[0]])
                 print ds+' '+dt
                 WorkPermutationList=[]
                 Smallestdivisors=[]

            if Time >= J:
                sys.exit(0)




