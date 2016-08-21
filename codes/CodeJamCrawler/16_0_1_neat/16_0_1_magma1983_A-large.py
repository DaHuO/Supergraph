#!/usr/bin/env python

# Problem A-large

filein = open("A-large.in","r")
fileout = open("A-large.out","w")

ncases = int(filein.readline())

for cases in range(ncases):
 digits=["0","1","2","3","4","5","6","7","8","9"]
 prod=1
 x = filein.readline()
 while (len(digits)!=0):
  xx=str(int(x)*prod)
  if (xx=="0"):
   break
  else:
   op1 = len(xx)
   for j in range(op1):
    if xx[j] in digits:
     digits.remove(digits[digits.index(xx[j])])
    else:
     pass
   prod+=1
 ans=xx
 if ans=="0":
  fileout.write("Case #%d: INSOMNIA\n" % (cases+1))
 else:
  fileout.write("Case #%d: %s\n" % (cases+1,ans))

filein.close()
fileout.close()