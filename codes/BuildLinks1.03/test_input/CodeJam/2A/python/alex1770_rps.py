import sys

def count(t,s): return len(filter(lambda x:x==s,t))

def thing(N,R,P,S):
  sts=[]# final strings
  d={'R':'RS','S':'SP','P':'PR'}# reverse map
  al='Z'# alphabetically minimal answer
  for w in "RPS":# winner
    t=w
    for n in range(N):
      s=""
      for x in t: s+=d[x]
      t=s
    if R==count(t,'R') and P==count(t,'P') and S==count(t,'S'):
      for n in range(N):
        # Sort 2^(N-n-1) pairs of 2^n into 2^(n+1)
        u=""
        for k in range(0,1<<N,1<<(n+1)):
          u0=t[k:k+(1<<n)]
          u1=t[k+(1<<n):k+(2<<n)]
          if u0<u1: u+=u0+u1
          else: u+=u1+u0
        t=u
      if t<al: al=t
  if al=='Z': return "IMPOSSIBLE"
  return al

T=int(sys.stdin.readline())
for case in range(1,T+1):
  [N,R,P,S]=[int(y) for y in sys.stdin.readline().strip().split()]
  print "Case #%d:"%case,thing(N,R,P,S)
