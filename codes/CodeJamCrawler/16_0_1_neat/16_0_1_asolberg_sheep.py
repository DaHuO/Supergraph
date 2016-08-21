#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(1500)

def doNum(n, num, progress):
  n = n+1
  newNum = n*num
  #print("n = " + str(n))
  #print("num = " + str(newNum))
  #print("progress = " + str(progress))
  if int(num) == 0:
  #  print("CC")
    return "INSOMNIA"
  for j in [int(i) for i in str(newNum)]:
    if int(j) in progress:
      progress.remove(int(j))
  if len(progress) == 0:
  #  print("AA")
    return newNum
  elif n >= 100:
  #  print("DD")
    return "INSOMNIA"
  else:
  #  print("recursing with n = " + str(n))
    return doNum(n, num, progress)
  #print("EE")

def solve(cipher):
  numbers_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  #print("running solve")
  return doNum(0, int(cipher), numbers_array)

if __name__ == "__main__":
  testcases = input()
   
  for caseNr in xrange(1, testcases+1):
    cipher = raw_input()
    #print("ground zero")
    print("Case #%i: %s" % (caseNr, solve(cipher)))
