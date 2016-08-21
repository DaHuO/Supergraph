#!/usr/bin/env/ python2.7

import sys
import time

def checkforallints(numset):
   values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   for val in values:
      if val not in numset:
        return False
   return True

testfile=open("testlarge.txt", 'r')

numtest=testfile.readline()

for i in range(int(numtest)):
   T=testfile.readline()
   sets=set()

   for number in str(T).rstrip():
      sets.add(int(number))

   v=2
   if int(T)==0:
      newval="INSOMNIA"
   else:
      #get start time
      starttime=time.time()
      while not checkforallints(sets):
	 newval=v*int(T)
	 for number in str(newval):
	    sets.add(int(number))
	 v+=1
	 #get curr time
	 currtime=time.time()
	 timepassed=(currtime-starttime)/60
	 if timepassed>=240:
	    newval="INSOMNIA"
	    break

   print "Case #{0}: {1}".format(i+1, newval)


