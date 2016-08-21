

T = int(raw_input())
for i in xrange(T):
  K, C, S = [int(x) for x in raw_input().strip().split()]
  print "Case #%d: %s" % (i + 1, ' '.join([str(x) for x in xrange(1, S + 1)]))