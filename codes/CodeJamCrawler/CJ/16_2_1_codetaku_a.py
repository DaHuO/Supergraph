#!/usr/bin/env python

import sys
import math
import Queue as q
import copy

lib = {} #mutable globals just in case
lst = []

words = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" }

if (len(sys.argv) != 3):
  print "You need 3 args including the file name"

def listSort(lst):
  return lst[0] #in case you need to sort a list of lists by first element of each

linesPerTest = int(sys.argv[2])

def retOpen(tnum):
  return "Case #" + str(tnum) + ":"

def runTest(t,lines,output):
  tmp = lines[0]
  scrambled = []
  for a in tmp:
    scrambled.append(a)
  val = ""
  try:
    while (scrambled.index("Z") != -1):
      val += "0"
      scrambled.remove("Z")
      scrambled.remove("E")
      scrambled.remove("R")
      scrambled.remove("O")
  except:
    pass
  try:
    while (scrambled.index("W") != -1):
      val += "2"
      scrambled.remove("T")
      scrambled.remove("W")
      scrambled.remove("O")
  except:
    pass
  try:
    while (scrambled.index("X") != -1):
      val += "6"
      scrambled.remove("S")
      scrambled.remove("I")
      scrambled.remove("X")
  except:
    pass  
  try:
    while (scrambled.index("S") != -1):
      val += "7"
      scrambled.remove("S")
      scrambled.remove("E")
      scrambled.remove("V")
      scrambled.remove("E")
      scrambled.remove("N")
  except:
    pass  
  try:
    while (scrambled.index("V") != -1):
      val += "5"
      scrambled.remove("F")
      scrambled.remove("I")
      scrambled.remove("V")
      scrambled.remove("E")
  except:
    pass
  try:
    while (scrambled.index("F") != -1):
      val += "4"
      scrambled.remove("F")
      scrambled.remove("O")
      scrambled.remove("U")
      scrambled.remove("R")
  except:
    pass  
  try:
    while (scrambled.index("O") != -1):
      val += "1"
      scrambled.remove("O")
      scrambled.remove("N")
      scrambled.remove("E")
  except:
    pass  
  try:
    while (scrambled.index("N") != -1):
      val += "9"
      scrambled.remove("N")
      scrambled.remove("I")
      scrambled.remove("N")
      scrambled.remove("E")
  except:
    pass  
  try:
    while (scrambled.index("I") != -1):
      val += "8"
      scrambled.remove("E")
      scrambled.remove("I")
      scrambled.remove("G")
      scrambled.remove("H")
      scrambled.remove("T")
  except:
    pass  
  try:
    while (scrambled.index("E") != -1):
      val += "3"
      scrambled.remove("T")
      scrambled.remove("H")
      scrambled.remove("R")
      scrambled.remove("E")
      scrambled.remove("E")
  except:
    pass
  print val
  val = ''.join(sorted(val))
  ret = retOpen(t) + " " + str(val) + "\n"
  output.write(ret)
  print ret

with open(sys.argv[1],"r") as file1, open("/home/codetaku/Downloads/output","w") as file2:
  testCase = 1
  lines = file1.readlines()
  numTests = int(lines[0])
  lineno = 1
  while (testCase <= numTests):
    if (linesPerTest > 0):
      runTest(testCase,lines[lineno:lineno + linesPerTest],file2)
      lineno += linesPerTest
    else:
      thisTestLines = int(lines[lineno].split(" ")[0]) + 1
      runTest(testCase,lines[lineno:lineno + thisTestLines],file2)
      lineno += thisTestLines
    testCase += 1






