def ipow(A,B):
  x = 1
  for i in range(B): x*=A
  return x

cases = int(raw_input())
for case in range(cases):
  K, C, S = map(int, raw_input().split())
  dist = 1
  level = C
  while level > 1:
    level-=1
    dist*=K
    dist+=1
  res = []
  i = 1
  l = ipow(K,C)
  #print dist, l
  while i <= l:
    res.append(i)
    i += dist
  print "Case #%d: %s" %(case+1, ' '.join(map(str,res)) )
  assert len(res) == S


