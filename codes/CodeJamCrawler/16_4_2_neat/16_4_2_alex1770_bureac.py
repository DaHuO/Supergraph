import sys

def prob(l):
  pl=[1]
  for p in l:
    q=1-p
    pl1=[]
    for i in range(len(pl)+1): pl1.append((pl[i] if i<len(pl) else 0)*q+(pl[i-1] if i>0 else 0)*p)
    pl=pl1
  return pl[len(l)/2]

def thing(N,K,sums):
  pp.sort()
  pmax=0
  for l in range(K+1):
    p=prob(pp[:l]+pp[N-(K-l):])
    if p>pmax: pmax=p
  return pmax

T=int(sys.stdin.readline())
for case in range(1,T+1):
  [N,K]=[int(y) for y in sys.stdin.readline().strip().split()]
  pp=[float(y) for y in sys.stdin.readline().strip().split()]
  print "Case #%d:"%case,thing(N,K,pp)
