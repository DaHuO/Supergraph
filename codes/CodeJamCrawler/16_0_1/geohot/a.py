T = int(raw_input())
for i in xrange(T):
  N = int(raw_input())
  d = set()
  n = 0

  if N == 0:
    n = "INSOMNIA"
  else:
    while len(d) != 10:
      n += N
      for dd in map(int, list(str(n))):
        d.add(dd)

  print "Case #%d:" % (i+1), n

