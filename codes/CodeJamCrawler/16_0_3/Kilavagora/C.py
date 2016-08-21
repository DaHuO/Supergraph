#!/usr/bin/python3

import fileinput
from sympy import isprime
from sympy.ntheory import factorint
f=fileinput.input()
T=int(f.readline())

for case in range(T):
  
  N,J=map(int,f.readline().split())
  count=0
  lead=2<<(N-2)
  
  print("Case #"+str(case+1)+":")
  
  for i in range(0,2<<(N-3)):    
    
    jamcoin=lead|(i<<1)|1
    valid=True
    jamstr=bin(jamcoin)[2:]
    factor_list=9*[0]
    
    for base in range(2,11):
      to_test=int(jamstr,base) if base>2 else jamcoin
      if isprime(to_test)==True:
        valid=False
        break
      factor_list[base-2]=(next (iter (factorint(to_test).keys())))

    if valid==True:
      count+=1
      print(jamstr,*factor_list)
    if J==count:
      break
      
      