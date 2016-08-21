#!/usr/bin/python
# -*- coding: utf-8 -*-
# @file   digit.py  
# @brief  Google Code Jam 2016 - Round 1B - Problem A
# @author Laurent Sauvage <sauvage_laurent@hotmail.com>
 
# -------
# Imports
# -------
import sys          # For argv[], exit(), etc
from os import path # For abspath()
import itertools    # For permutations()
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

   NUMALPHA= (
              ('Z', "ZERO" ,'0'),
              ('W', "TWO"  ,'2'),   
              ('X', "SIX"  ,'6'),   
              ('G', "EIGHT",'8'), 
              ('T', "THREE",'3'), 
              ('S', "SEVEN",'7'), 
              ('V', "FIVE" ,'5'),  
              ('F', "FOUR" ,'4'), 
              ('I', "NINE" ,'9'),  
              ('N', "ONE"  ,'1')
             )   

   for l in fdIn:
      nums= [] # Empty list to store nums

      line= list(l.rstrip())
#     print "DEBUG line=", line
      while len(line)!=0:
         for single, string, integer in NUMALPHA:
            if single in line:
#              print "DEBUG Found ", single
               nums.append(integer)
               for digit in string: line.remove(digit)
#              print "DEBUG line removed", line
               break
   
      nums.sort()
#     print "DEBUG nums=", nums
      y= ''
      for elem in nums: y+=str(elem)
      line= "Case #{0}: {1}\n".format(nTest, y)
      print line,
      fdOut.write(line)

      nTest+= 1
 
   # Termination
   fdIn .close()
   fdOut.close()
