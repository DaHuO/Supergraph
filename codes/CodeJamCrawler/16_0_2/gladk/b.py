#!/usr/bin/env python3

import os, numpy, math, sys, string

infile = open(sys.argv[1],"r")
lines = infile.readlines()
infile.close()

T=int(lines[0])
output = ''

curLine=1
output = ""
for t in range(T):
  s=str(lines[curLine].strip())
  
  output+= "Case #%d: "%(t+1)
  answ = 0
  
  change = 0
  for i in range(1,len(s)):
    if (s[i-1]!=s[i]):
      change+=1
  
  if (s[-1] == '-'):
    change+=1
  
  output += "%d\n"%change
  
  curLine+=1
  
#print (output)
open(sys.argv[1]+'.res','w').write(output)
