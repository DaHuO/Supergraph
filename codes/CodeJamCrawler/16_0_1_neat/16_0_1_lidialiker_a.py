from collections import Counter

def bleatrix(n):
    if n == 0:
        return 'INSOMNIA'
    c = 1
    ctr = Counter()

    while True:
        it = c * n
        ctr.update(list(str(it)))

        if 0 not in ctr.values() and len(ctr.values()) == 10:
            return it

        c += 1

with open('A-large.in') as f:
    N = int(f.readline().strip())
    for i in xrange(N):
        n = int(f.readline().strip())
        print "Case #%d: %s" % (i + 1, bleatrix(n))
