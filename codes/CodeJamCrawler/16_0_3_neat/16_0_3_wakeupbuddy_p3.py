import sys,os
import time
import math
def is_prime(num):
   if num < 2:
      return -1
   for x in range(2, num/2 + 1):
      if num % x == 0:
         return x
   return -1

def is_prime2(num):
   if num < 2:
      return -1
   for x in plist:
      if num % x == 0:
         return x
   return -1


def generatePrimes():
   D = {}
   q = 2
   while True:
      if q not in D:
         yield q
         D[q*q] = [q]
      else:
         for p in D[q]:
            D.setdefault(p+q, []).append(p)
         del D[q]
      q += 1

def getFactorList(N):
   ret = []
   for base in range(2, 11):
      realNum = int(str(N), base)
      res = is_prime(realNum)
      if res < 0:
         return ret
      else:
         ret.append(res)
   return ret

def getFactorList2(N, plist):
   ret = []
   for base in range(2, 11):
      realNum = int(str(N), base)
      res = realNum in plist
      if res == True: # prime
         return ret
      else:
         factor = is_prime2(realNum)
         if factor<0:
            return ret
         else:
            ret.append(is_prime2(realNum))
   return ret


def formatRet(thisN, factorList):
   retStr = str(thisN)
   for i in factorList:
      retStr = retStr + " " + str(i)
   return retStr

N = 6
J = 3
b = ""
for i in range(0, N):
   b = b + "1"
upp = math.floor(math.sqrt(int(b))) + 10
t = time.time()

plist = []
for i in generatePrimes():
   plist.append(i)
   if i > upp:
      break
elapsed = time.time() - t
#print(plist)
#print("time: ", elapsed)
#print("intb: ", int(b))
#print("upp: ", upp)
#sys.exit()

binary = lambda n: '' if n==0 else binary(n/2) + str(n%2)
retCnt = 0
print("Case #1:")
for i in range(0, 2**(N-2)):
   thisN = int('1' + binary(i).zfill(N-2) + '1')
   #print(thisN)
   factorList = getFactorList2(thisN, plist)
   if len(factorList) == 9:
      retStr = formatRet(thisN, factorList)
      retCnt = retCnt + 1
      print(retStr)
   if retCnt >= J:
      break
