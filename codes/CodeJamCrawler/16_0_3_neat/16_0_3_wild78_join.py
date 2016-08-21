#!/usr/bin/python
# -*- coding: utf-8 -*-
# @file   join.py 
# @brief  Google Code Jam 2016 - Problem C
# @author Laurent Sauvage <sauvage_laurent@hotmail.com>
 
# -------
# Imports
# -------
import sys          # For argv[], exit(), etc
from os import path # For abspath()

# ---------
# Functions
# ---------
def isPrime(n, testLimit):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  cpt= 0
  while f <= r and cpt<testLimit:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
    cpt+= 1
  return True  

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
   _= fdIn.readline().rstrip() # Number of tests (useless with Python, and with this problem...)

   N, J= map(int, fdIn.readline().split())
   jam_l= [] # Empty list to store jamcoins
   offset= 2**(N-1)
   j= 0
   for i in xrange(1,2**(N-1),2):
      form= "{0:0"+str(N-2)+"b}"
      jamBinStr= form.format(offset+i)
      divisors_l= [] # Empty list to store divisor of current jam 
      for base in xrange(2,11):
         jam= long(jamBinStr, base)
         if isPrime(jam, 10000):
            break
         else:
            i= 3
            while i<10000:
               if jam%i==0:
                  if i not in divisors_l:
                     divisors_l.append(i)
                     break
               i+= 2

      if len(divisors_l)==9: jam_l.append((jamBinStr, divisors_l))
      if len(jam_l)==J: break

   line= "Case #1:\n"
   for jam, div_l in jam_l:
      line+= jam
      for div in div_l:
         line+= ' {0}'.format(div)
      line+= '\n' 
   fdOut.write(line)
 
   # Termination
   fdIn .close()
   fdOut.close()
