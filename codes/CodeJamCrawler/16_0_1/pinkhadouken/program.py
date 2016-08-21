
t = int(raw_input())


for i in xrange(t):
  n = int(raw_input())
  
  l = set()

  it = 0
  while len(l) < 10:
    it += 1

    sn = str(n * it)

    for d in sn:
      l.add(d)

    if it > 100:
      sn = 'INSOMNIA'
      break
  
  print "Case #{}: {}".format(i+1, sn)