#!/usr/bin/python3
import fileinput
f=fileinput.input()
T=int(f.readline())

for case in range(T):
  K,C,S=map(int,f.readline().split())
  rep=K**(C-1)
  if S>0:
   print("Case #"+str(case+1)+":",*[1+i*rep for i in range(S)])
  else:
   print("Case #"+str(case+1)+":","IMPOSSIBLE")
    
