precalc = {0: 'INSOMNIA', 1: 10, 2:90, 3:30, 4:92, 5:90, 6:90, 7:70, 8:96, 9:90}
f = open('A-large.in', 'r')
t = int (f.readline())

for i in xrange(1, t + 1):
  seen = [0,0,0,0,0,0,0,0,0,0]
  count = 0
  val = int(f.readline())
  if val in precalc:
    print "Case #{}: {}".format(i, precalc[val])
  else:
    orig = val
    while val%10 == 0:
      if val == 0:
        break
      seen[0]=1
      count = 1
      val = val/10
    curr = 0
    j = 1
    while j<999:
      curr += val
      for ch in str(curr):
        ind = int(ch)
        if seen[ind] == 0:
          seen[ind] = 1
          count+=1
        if count == 10: break 
      if count == 10: break 
      j+=1

    print "Case #{}: {}".format(i, j*orig)
    # check out .format's specification for more formatting options
