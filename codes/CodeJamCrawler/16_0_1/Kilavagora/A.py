#!/usr/bin/python3
import fileinput
f=fileinput.input()
T=int(f.readline())


for case in range(T):
  
  N=int(f.readline())
  
  if N==0:
    print("Case #"+str(case+1)+":","INSOMNIA")
    continue
  
  curr=N
  mset=set(str(N))
  while len(mset)<10:
    curr+=N
    mset.update(str(curr))
        
  print("Case #"+str(case+1)+":",curr)

     