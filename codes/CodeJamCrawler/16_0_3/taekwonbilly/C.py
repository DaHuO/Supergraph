from math import *

cases = int(raw_input())
for case in range(cases):
  N, J = map(int,raw_input().split())
  print "Case #%d:" %(case+1 )

  cnt = 0
  for i in xrange(2**(N-2)):
    bs = bin(i)[2:]
    bs = '1' + (N-2-len(bs))*'0' + bs + '1'
    div = [-1]*11
    for i in range(2, 11):
      num = int(bs, i)
      for j in xrange(2, int(1+sqrt(num))):
        if num % j == 0:
          div[i] = j
          break
      if div[i] == -1: break
    if div.count(-1) == 2:
      #print [int(bs,i) for (i,s) in enumerate(div) if i >= 2]
      print bs, ' '.join(map(str,div[2:]))
      cnt+=1
      if cnt == J: break
