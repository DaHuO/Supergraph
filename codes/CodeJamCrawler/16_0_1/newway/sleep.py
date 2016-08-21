#! /usr/bin/env python
import sys

def num_sleep(n):
  if n ==0:
    return "INSOMNIA"

  seen = set()
  for i in range(1,100):
    num = i * n
    #print(num)
    for d in str(num):
      seen.add(d)
    #all digits seen!
    if len (seen) == 10: 
      return num
  return "INSOMNIA"

with open (sys.argv[1]) as f:
  cases = int(f.readline())
  for case in range(cases):
    num = int(f.readline())
    last= num_sleep(num)
    print("Case #%d: %s"%(case+1, last))

'''
for i in range(210):
  last= num_sleep(i)
  print ("last num=",last)
'''  