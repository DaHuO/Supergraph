from sys import stdin

for i in xrange(int(stdin.readline())):
    (K,C,S) = tuple(int(z) for z in stdin.readline().split())
    print "Case #%d: %s" % (i + 1, " ".join(str(v) for v in xrange(1,K+1)))
