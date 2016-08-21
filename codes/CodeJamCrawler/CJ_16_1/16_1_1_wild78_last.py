#!/usr/bin/python
# -*- coding: utf-8 -*-
# @file   last.py 
# @brief  Google Code Jam 2016 - Round 1A - Problem A
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

      first= True
      y= ''
      for c in l.strip():
         if first:
            first= False
            y= c
         else:
            if ord(c)>=ord(y[0]): y= c+y
            else:                y= y+c

      line= "Case #{0}: {1}\n".format(nTest, y)
      print line,
      fdOut.write(line)

      nTest+= 1
 
   # Termination
   fdIn .close()
   fdOut.close()
