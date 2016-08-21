#!/usr/bin/python3
import fileinput
f=fileinput.input()
T=int(f.readline())
    
for case in range(T):
  S=f.readline().strip()
  left=S[0]
  right=S[0]
  out=[left]
  for c in S[1:]:
    if c>=left:
      out=[c]+out
      left=c
    else:
      out+=[c]
      right=c  
  
  print("Case #"+str(case+1)+":",''.join(out))
    
