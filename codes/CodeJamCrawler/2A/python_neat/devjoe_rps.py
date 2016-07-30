from types import *

seq=["PR","P","PS","S","RS","R"]

def getplayers(x):
  if type(x)==StringType:
    return x
  res=""
  for y in x:
    res+=getplayers(y)
  return res

t=input()
for j in xrange(t):
  n,r,p,s=map(int,raw_input().strip().split())
  mx=max((r,p,s))
  mn=min((r,p,s))
  if mx-mn>1:
    print "Case #"+str(j+1)+": IMPOSSIBLE"
    continue
  #Find which types we have more of
  more=""
  if p==mx:
    more+="P"
  if r==mx:
    more+="R"
  if s==mx:
    more+="S"
  #Simulate N rounds
  pos=seq.index(more)
  winner=seq[(pos+n)%6]
  #Generate needed contests each round.
  tree=[winner]
  contests=[[tree]]
  for rnd in xrange(n):
    contests.append([])
    for contest in contests[-2]:
      for player in xrange(len(contest)):
        if contest[player]=="P":
          contest[player]=["P","R"]
        elif contest[player]=="R":
          contest[player]=["R","S"]
        else:
          contest[player]=["P","S"]
        contests[-1].append(contest[player])
  #Sort contests
  for jj in xrange(len(contests)-1,-1,-1):
    for contest in contests[jj]:
      contest.sort()
  #retrieve all players in order
  res=getplayers(tree)
  print "Case #"+str(j+1)+": "+res
