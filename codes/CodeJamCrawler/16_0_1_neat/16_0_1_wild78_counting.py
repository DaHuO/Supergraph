#!/usr/bin/python
# -*- coding: utf-8 -*-
# @file   counting.py 
# @brief  Google Code Jam 2016 - Problem A
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
   _= fdIn.readline().rstrip() # Number of tests (useless with Python...)
   nTest= 1
   for l in fdIn:
      digits_l= [] # Empty list to store digits
      i= 1
      N= int(l)
      if N==0: y= "INSOMNIA"
      else:
         ASLEEP= False
         while not ASLEEP:
            y= i*N
            for digit in str(y):
               if digit not in digits_l: digits_l.append(digit)
            if len(digits_l)==10:
               ASLEEP= True
            else:
               i+= 1
      print "Case #{0}: {1}".format(nTest, y)
      nTest+= 1
 
   # Termination
   fdIn .close()
   fdOut.close()
