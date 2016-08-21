#!/usr/bin/env python
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  num=input()
  counter=0
  if(num==0):
    ans="INSOMNIA"
  else:
    digits= 10*[False]
    loop=True
    multi=0
    while(loop):
      multi+=1
      counter+=1
      numLoop=num*multi
   
      while(numLoop!=0 and digits.count(True)!=10):
        digit=numLoop%10
        digits[digit]=True
        
        numLoop/=10

      if(digits.count(True)==10):
        loop=False
        ans=num*multi
      
         
  print("Case #{}: {}".format(i,ans ))
  # check out .format's specification for more formatting optionsa

