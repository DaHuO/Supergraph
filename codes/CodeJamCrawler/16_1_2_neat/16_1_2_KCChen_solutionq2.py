
t = int(raw_input())  # read a line with a single integer
for p in xrange(1, t + 1):
    
  N=int(raw_input())
  lines=[]
  for x in xrange(1,2*N):
      lines.extend([int(s) for s in raw_input().split(" ")])

  solder=[]
  for i in xrange(len(lines)):
      if lines[i] in solder:
          solder.remove(lines[i])
      else:
          solder.append(lines[i])
#      for j in xrange(len(lines[0])):
#          if lines[i][j] in lines:
#              solder.remove(lines[i][j])
#          else:
#              solder.append(lines[i][j])
  solder=sorted(solder)
  solder=[str(s) for s in solder]

  print "Case #{}: {}".format(p," ".join(solder))
