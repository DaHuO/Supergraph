from sys import stdin

stream = stdin
N = int(stream.readline().strip())

def check(n):
    s = set()
    i = 1
    if n==0:
        print 'INSOMNIA'
        return
    while True:
        for c in str(i*n):
            s.add(c)
        if len(s)==10:
            print i*n
            break
        i += 1
    else:
        print 'INSOMNIA'

for i in xrange(N):
    n = int(stream.readline().strip())
    print "Case #" + str(i+1) + ':',
    check(n)
