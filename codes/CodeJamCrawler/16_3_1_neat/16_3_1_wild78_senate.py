#!/usr/bin/python
# -*- coding: utf-8 -*-
# @file   senate.py
# @brief  Google Code Jam 2016 - Round 1C - Problem A
# @author Laurent Sauvage <sauvage_laurent@hotmail.com>
 
# -------
# Imports
# -------
import sys          # For argv[], exit(), etc
from os import path # For abspath()

# ----
# Main
# ----
if __name__ == "__main__":

   # Initialization
   try:
      IFILE= path.abspath(sys.argv[1])

   except IndexError:
      print "Usage: %s <IFILE>" % path.basename(sys.argv[0])
      sys.exit(2) # Command line syntax error

   fdIn = open(IFILE, 'r')
   OFILE= IFILE.replace(".in",".out")
   fdOut= open(OFILE, 'w')

   # Processing
   nCase= int(fdIn.readline()) # Number of tests (useless with Python...)
   for nTest in range(1, nCase+1):
      N= int(fdIn.readline())
      senators= map(int, fdIn.readline().rstrip().split())
      print "DEBUG N={0} -- senators={1}".format(N, senators)

      y= ''
      while sum(senators)!=0:
         # Find maximum values
         Max= max(senators)
         iMax= []
         for i in range(len(senators)):
            if senators[i]==Max:
               iMax.append(i)
#        print "DEBUG max={0} at {1}".format(Max, iMax)

         # Update senators
         if y!='': y+= ' '
#        if len(iMax)==1: # Single max, substract 2
#           index= iMax[0]
#           if sum(senators)%2==0:
#              senators[index]-= 2
#           else:
#              senators[index]-= 1
#           y+= chr(65+index)*2
#        else:
         for i in range(len(iMax)):
            index= iMax[i]
            senators[index]-= 1
            y+= chr(65+index)
            if i!=len(iMax)-1:
               if len(iMax)%2==1 and i%2==0: y+= ' '
               if len(iMax)%2==0 and i%2==1: y+= ' '

         print "DEBUG new senators={0}".format(senators)

      line= "Case #{0}: {1}\n".format(nTest, y)
      print line,
      fdOut.write(line)
 
   # Termination
   fdIn .close()
   fdOut.close()
