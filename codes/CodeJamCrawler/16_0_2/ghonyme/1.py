#!/usr/bin/python

import sys
def allMinus(ch):
  return ch.count("-") == len(ch)

def allPlus(ch):
  return ch.count("+") == len(ch)

def reverseSign(ch,i):
  li = list(ch)
  if li[i] == "+":
    li[i] = "-"
  else:
    li[i] = "+"
  
  return li

def getSameFromBegin(ch):
  res = 1
  i = 0
  li = list(ch)
  while li[i] == li[i+1]:
    res = res +1
    i=i+1
  return res

ch = sys.argv[1]
nb=0
i=0
while True:
  if allMinus(ch):
    nb = nb+1
    break
  elif allPlus(ch):
    break
  else:
    for i in range(0,getSameFromBegin(ch)):
      ch = "".join(reverseSign(ch,i))    
  nb = nb+1
print nb

