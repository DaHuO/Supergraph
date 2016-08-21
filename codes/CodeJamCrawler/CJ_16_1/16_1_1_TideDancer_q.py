import numpy

t = int(raw_input())  # read a line with a single integer

for j in xrange(1, t + 1):
  S = [str(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  S = str(S[0])
  r = []
  r.append(S[0])
  for i in range(1,len(S)):
    if S[i] >= r[0]:
      r.insert(0, S[i])
    else:
      r.append(S[i]) 
    
  print "Case #{}: {}".format(j, ''.join(str(x) for x in r))
