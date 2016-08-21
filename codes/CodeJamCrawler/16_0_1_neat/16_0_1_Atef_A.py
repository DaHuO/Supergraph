
inp = open("A-large.in")
T = int(inp.readline().strip())
for _t in xrange(T):
  N = int(inp.readline().strip())
  ans = N
  digs = [False] * 10
  if N == 0:
    ans = "INSOMNIA"
  else:
    i = 2
    while True:
      x = N
      while x > 0:
        digs[x % 10] = True
        x /= 10
      if all(d for d in digs):
        ans = N
        break
      N += ans
  print "Case #%d: %s" % (_t + 1, str(ans))

#for i in xrange(101): print i
