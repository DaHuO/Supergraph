#!/usr/bin/env python3

import os, numpy, math, sys, string

def ret(n):
  ns = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
  i = 1
  while (i < 100000000):
    N=n*i
    nT = N
    while nT:
      nD = nT % 10
      if nD in ns:
        ns.remove(nD)
      nT = nT // 10
    if len(ns) == 0:
      return (N)
    i+=1
  return (0)

infile = open(sys.argv[1],"r")
lines = infile.readlines()
infile.close()

T=int(lines[0])
output = ''

curLine=1
output = ""
for t in range(T):
  N=int(lines[curLine].split()[0])
  output+= "Case #%d: "%(t+1)
  answ = ret(N)
  if (answ==0):
    output += "INSOMNIA\n"
  else:
    output += "%d\n"%answ
  
  #print (ret(N))
  curLine+=1
  

open(sys.argv[1]+'.res','w').write(output)
