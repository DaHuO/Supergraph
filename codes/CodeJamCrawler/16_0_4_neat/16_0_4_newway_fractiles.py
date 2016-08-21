#! /usr/bin/env python
import sys




with open (sys.argv[1]) as f:
  cases = int(f.readline())
  for case in range(cases):
    look = list()
    k, c, s = f.readline().strip().split(" ")
    k = int(k)
    c = int(c)
    s = int(s)
    total = k ** c
    #print("k=%d, c=%d, s=%d, totaltiles=%d"%(k,c,s,total))
    idx = int(total / k)
    for i in range(k):
      look.append(str(i*idx+1))
    print ("Case #%d: %s" %(case+1, ' '.join(look)))
