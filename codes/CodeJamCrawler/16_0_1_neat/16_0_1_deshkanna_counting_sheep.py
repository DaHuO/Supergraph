t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input())  # input num
  o = n
  s = set(str(n))
  if n == 0: o = 'INSOMNIA'
  else:
    while (len(s)!=10):
      o+=n
      s|=set(str(o))
  print "Case #{}: {}".format(i, o)
