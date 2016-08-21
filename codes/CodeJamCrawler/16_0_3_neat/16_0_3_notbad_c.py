#!/usr/bin/python

num=0;
st = (2**31) + 1
print "Case #1:"
while num < 500:
  #print bin(st)[2:]
  factor = [0 for i in range(0, 11)]
  cnt = 1
  for i in range(2, 11):
    v = int(bin(st)[2:], i)
    for j in range(2, 100000):
     # print v, j, v % j
      if ((v % j == 0)):
          factor[i] = j
          cnt = cnt+1;
          break;
    if cnt != i:
      break 
  if (cnt == 10):
    print bin(st)[2:],
    num = num+1
    for i in range(2, 11):  
      print factor[i],
    print
  st = st + 2

