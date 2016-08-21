n = int(raw_input())

for a in xrange(0, n):
  x = int(raw_input())
  if x == 0:
    print "Case #{}: INSOMNIA".format(a+1)
    continue
  else:
    q = [0,1,2,3,4,5,6,7,8,9]
    buf = 1
    while True:
      z = str(buf * x)
      for b in z:
        if q[ int(b) ] != -1:
          q[ int(b) ] = -1
      z = set(q)

      if len(z) == 1:
        print "Case #{}: {}".format(a+1,buf * x)
        break
      buf = buf + 1
