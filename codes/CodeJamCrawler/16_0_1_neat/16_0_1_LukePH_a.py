#!/usr/bin/python
import sys
import datetime as dt
from datetime import datetime


caseIndex=0
out = open('out','w')

with open(sys.argv[1]) as f:
  
  numTestCases=f.readline()
  
  while True:
    line = f.readline()
    if not line:
        break
     
    line=line.strip()
    
    #print (line)
    baseNum=int(line)
    digits=[0,1,2,3,4,5,6,7,8,9]
    result="INSOMNIA"
    for count in xrange(1,99999):
      current=baseNum*count
      for d in digits[:]:
        if str(d) in str(current):
          digits.remove(d)
      
      if len(digits)==0:
        result=current
        break;
    
    caseIndex+=1
    out.write ("Case #"+str(caseIndex)+": "+str(result)+"\n")#*
    
    
    
