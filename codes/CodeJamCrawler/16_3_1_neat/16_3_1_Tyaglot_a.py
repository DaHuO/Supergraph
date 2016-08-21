alp=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def valid(parties):
  s=sum(parties)
  for i in parties:
    if i>s/2 or i<0:
      return False
  return True



def solve(parties):
  if valid(parties) and sum(parties)==0:
    return []
  for k in range(len(parties)):
    m=sorted(parties)[-(k+1)]
    m=[i for i,j in enumerate(parties) if j==m]
    for n in m:
      parties[n]-=2
      if valid(parties):
        tmp=solve(parties)
        if tmp!=None:
          return [alp[n]*2]+tmp
      parties[n]+=2
      parties[n]-=1
      if valid(parties):
        tmp=solve(parties)
        if tmp!=None:
          return [alp[n]]+tmp
      for x in range(len(parties)):
        parties[x]-=1
        if valid(parties):
          tmp=solve(parties)
          if tmp!=None:
            return [alp[n]+alp[x]]+tmp
        parties[x]+=1
      parties[n]+=1
        
      
  return None
      
      
      
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  raw_input()
  parties=[int(k) for k in raw_input().split(' ')]
  print "Case #"+str(i)+": "+' '.join(solve(parties))



        
    
