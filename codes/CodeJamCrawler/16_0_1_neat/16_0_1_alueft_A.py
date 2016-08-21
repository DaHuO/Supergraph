t = int(raw_input())
for T in xrange(1,t+1):
  n = int(raw_input())
  if not n:
    print "Case #{0}: INSOMNIA".format(T)
    continue
  x = [False]*10
  l = 0
  while True:
    d = True
    for i in x:
      if not i:
        d = False
        break
    if d:
      print "Case #{0}: {1}".format(T,l)
      break
    l += n
    for i in str(l):
      x[ord(i)-ord("0")] = True
