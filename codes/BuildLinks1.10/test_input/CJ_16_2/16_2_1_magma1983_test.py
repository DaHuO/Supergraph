#!/usr/bin/env python

filein = open("test.in","r")
fileout = open("test.out","w")

cases = int(filein.readline())
nums=["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

for i in range(0,cases,1):
 x=filein.readline().rstrip()
 x=list(x)
 numbers=[]
 if x.count("Z")>0:
  for j0 in range(x.count("Z")):
   numbers.append("0")
   x.remove("Z")
   x.remove("E")
   x.remove("R")
   x.remove("O")
 else:
  pass
 if x.count("W")>0:
  for j2 in range(x.count("W")):
   numbers.append("2")
   x.remove("T")
   x.remove("W")
   x.remove("O")
 else:
  pass
 if x.count("U")>0:
  for j4 in range(x.count("U")):
   numbers.append("4")
   x.remove("F")
   x.remove("O")
   x.remove("U")
   x.remove("R")
 else:
  pass
 if x.count("X")>0:
  for j6 in range(x.count("X")):
   numbers.append("6")
   x.remove("S")
   x.remove("I")
   x.remove("X")
 else:
  pass
 if x.count("G")>0:
  for j8 in range(x.count("G")):
   numbers.append("8")
   x.remove("E")
   x.remove("I")
   x.remove("G")
   x.remove("H")
   x.remove("T")
 else:
  pass

 if x.count("O")>0:
  for j1 in range(x.count("O")):
   numbers.append("1")
   x.remove("O")
   x.remove("N")
   x.remove("E")
 else:
  pass

 if x.count("T")>0:
  for j3 in range(x.count("T")):
   numbers.append("3")
   x.remove("T")
   x.remove("H")
   x.remove("R")
   x.remove("E")
   x.remove("E")
 else:
  pass

 if x.count("F")>0:
  for j5 in range(x.count("F")):
   numbers.append("5")
   x.remove("F")
   x.remove("I")
   x.remove("V")
   x.remove("E")
 else:
  pass

 if x.count("S")>0:
  for j7 in range(x.count("S")):
   numbers.append("7")
   x.remove("S")
   x.remove("E")
   x.remove("V")
   x.remove("E")
   x.remove("N")
 else:
  pass

 if x.count("I")>0:
  for j9 in range(x.count("I")):
   numbers.append("9")
   x.remove("N")
   x.remove("I")
   x.remove("N")
   x.remove("E")
 else:
  pass

 numbers.sort()
 ans="".join(numbers)
 fileout.write("Case #%d: %s\n" %(i+1,ans))

filein.close()
fileout.close()
