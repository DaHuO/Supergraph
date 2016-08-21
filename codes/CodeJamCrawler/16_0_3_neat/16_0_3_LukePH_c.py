#!/usr/bin/python
import sys
import datetime as dt
from datetime import datetime

startTimers={}
endTimers={}

def startTimer(name):
  startTimers[name]=datetime.now()

def endTimer(name):
  endTimers[name]=datetime.now()

def printTimers(f):
  for name in startTimers:
    f.write("Timer "+str(name)+" took:"+str(endTimers[name]-startTimers[name])+"\n")

def debug(text):
  print(text)
  #pass

def isNonPrime(num):
  for i in xrange(2,num):
    if (num % i) == 0:
      return i
      break
  else:
    return None

def isNonPrime2(n):
    if n < 2: return 1
    if n == 2: return None    
    if not n & 1: return 2
    for x in xrange(3, int(n**0.5) + 1, 2):
      if n % x == 0:
        return x
    return None

def intToBin(num):
  return "{0:b}".format(num)


caseIndex=0
out = open('out','w')
with open(sys.argv[1]) as f:
  numTestCases=f.readline()
  
  while True:
    line = f.readline()
    if not line:
        break
     
    line=line.strip()
    
    caseIndex+=1
    result=""
    output="Case #"+str(caseIndex)+": "+str(result)
    print(output)
    out.write (output+"\n")
    
    N,J=line.split(" ")
    N=int(N)
    J=int(J)
    
    foundCoins=0
    
    changingSize=N-2
    
    print("changingSize:"+str(changingSize))
    
    maxCoin=((changingSize)**2)
    print("maxCoin:"+str(maxCoin))
    for i in xrange(0, maxCoin ):
      numInBin="1"+intToBin(i).zfill(changingSize)+"1"
      
      foundPrime=False
      dividers=[]
      for base in range(2,11):
        baseNum=int(numInBin, base)
        divider=isNonPrime2(baseNum)
        if divider is None:
          foundPrime=True
          break
        dividers.append(str(divider))
      if not foundPrime:
        print ("No primes")
        output=numInBin+" "+" ".join( dividers )
        print(output)
        out.write (output+"\n")
        foundCoins+=1
        if foundCoins>=J:
          break
    
    
    
