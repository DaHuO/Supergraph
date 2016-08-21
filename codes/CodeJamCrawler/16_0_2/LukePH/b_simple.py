#!/usr/bin/python
import sys
import datetime as dt
from datetime import datetime

minFlips=None
minFlipsPath=None
printCounter=0

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

#brute force
def findMin(orginalPancakes, pancakes,currentFlips, path):
  global minFlips, minFlipsPath, printCounter
  if minFlips is not None:
    if minFlips<=currentFlips:
      return
  
  printCounter+=1
  if printCounter>9000:
    printCounter=0
    debug(str(pancakes)+":"+str(currentFlips))
  
  if not "-" in pancakes:
    debug(str(pancakes)+":"+str(currentFlips)+">> "+str(path))
    minFlips=currentFlips
    minFlipsPath=path
    return
  
  if minFlips is not None:
    if minFlips<=currentFlips+1:
      return
  
  if currentFlips>len(orginalPancakes)+1: #each flipped individually
    debug(str(pancakes)+":"+str(currentFlips))
    return
  
  startIndex=len(pancakes)
  skipping=True
  
  for n in xrange(startIndex,0,-1):
    if skipping:
      if pancakes[n-1]=="+":
        continue
      skipping=False
    
    if n<len(pancakes) and pancakes[n]==pancakes[n-1]:
      continue
    
    if "+-" in pancakes[n:] and "-+" in pancakes[:n]:
      continue
    
    newPancakes=flip(pancakes,n)
    
    if pancakes==newPancakes:
      continue
    
    if newPancakes in path:
      continue
    
    findMin(orginalPancakes, newPancakes,currentFlips+1,path+[newPancakes])


def flip(pancakes, at):
  top=reversed(pancakes[:at])
  bottom=pancakes[at:]
  flipped=""
  for p in top:
    if p=="-":
      flipped+="+"
    else:
      flipped+="-"
  return flipped+bottom
  
caseIndex=0
out = open('out','w')
with open(sys.argv[1]) as f:
  numTestCases=f.readline()
  
  while True:
    line = f.readline()
    if not line:
        break
     
    line=line.strip()
    minFlips=None
    pancakes=line
    
    startTimer("findMin")
    orginalPancakes=pancakes
    
    findMin(orginalPancakes, pancakes,0,[pancakes])
    endTimer("findMin")
    
    if minFlips is None:
      raise Exception("Failed on:"+str(pancakes))
    
    result=minFlips
    caseIndex+=1
    
    output="Case #"+str(caseIndex)+": "+str(result)
    
    
    out.write (output+"\n")
    
