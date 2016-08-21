import random
import sys
maxFac = 10000

def getfactor(n, cache = {}):
    if n <= 3:
        return 1
    if n in cache:
        return cache[n]
    for i in xrange(2, min(int(n ** 0.5) + 1, maxFac)):
        if n % i == 0:
            cache[n] = i
            return n
    cache[n] = 1
    return 1


def findJam(N):
    while True:
        rnd = sum(2 ** x for x in random.sample(range(N - 2), 4))
        s = '1' + bin(rnd)[2:].zfill(N - 2) + '1'
        #print s

        wrong = False
        fac = []
        for i in xrange(2, 11):
            n = int(s, i)
            f = getfactor(n)
            if f == 1 or f == n:
                wrong = True
                break
            fac.append(f)

        if not wrong:
            return s, fac




Tn = input()
for Tc in xrange(1, Tn + 1):
    N,J = map(int, raw_input().split())
    s = {}

    for i in xrange(J):
        print 'num_%d' % i
        sys.stdout.flush()
        while True:
            x, y = findJam(N)
            if x not in s:
                s[x] = y
                break

    print 'Case #%d:' % Tc

    for x,y in s.iteritems():
        print x, ' '.join(map(str, y))




