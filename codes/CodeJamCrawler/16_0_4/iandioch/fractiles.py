import sys

lines = sys.stdin.readlines()

n = int(lines[0])

for t in xrange(1, n+1):
    k, c, s = [int(x) for x in lines[t].split()]
    print 'Case #' + str(t) + ':',
    for i in xrange(1, k**c+1, k**(c-1)):
        print i,
    print ''
