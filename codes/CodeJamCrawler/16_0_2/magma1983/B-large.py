#!/usr/bin/env python

# Problem B-large

filein = open("B-large.in","r")
fileout = open("B-large.out","w")

ncases = int(filein.readline())

for cases in range(ncases):
 mp = list(filein.readline())
 op1 = len(mp)
 counter = 0
 final = ["+"]*op1
 while (mp!=final):
  if (mp[0]=="+"):
   if (mp.count("-")>0):
    op2 = mp.index("-")
    for i in range(0,op2,1):
     mp[i]="-"
    counter+=1
   else:
    break
  elif (mp[0]=="-"):
   if (mp.count("+")>0):
    op2 = mp.index("+")
    for i in range(0,op2,1):
     mp[i]="+"
    counter+=1
   else:
    counter+=1
    break
  else:
   break
 fileout.write("Case #%d: %d\n" % (cases+1, counter))

filein.close()
fileout.close()