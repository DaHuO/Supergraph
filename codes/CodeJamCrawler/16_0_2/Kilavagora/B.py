#!/usr/bin/python3
import fileinput
f=fileinput.input()
T=int(f.readline())

for case in range(T):
  pancakes=f.readline().strip()
  prev=pancakes[0]
  flips=1 if prev=="-" else 0
  for p in pancakes[1:]:
    if p==prev:
      continue
    prev=p
    if p=="-":
      flips+=2
        
  print("Case #"+str(case+1)+":",flips)

     