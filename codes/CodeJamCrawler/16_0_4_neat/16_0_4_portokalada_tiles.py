import sys

def solution(k,c,s):
  tiles=[]
  
  if k % c == 0:
    needed=k/c
  else:
    needed=k/c+1
  
  if needed>s:
    return tiles
  else:
    m=0
    for i in range(needed):
      a=0
      for j in range(c):
        a=a+(k**j)*m
        if m+1<k:
          m=m+1
        else:
          m=0
      tiles.append(a+1)
  return tiles

write = sys.stdout.write  
T=int(raw_input())

for i in range(1,T+1):
  k,c,s=map(int,raw_input().split())
  tiles=solution(k,c,s)
  if tiles==[]:
    print('Case #%d: IMPOSSIBLE' % i)
  else:
    write('Case #%d:' % i)
    for j in tiles:
      write(' %d' % j)
    print
 
