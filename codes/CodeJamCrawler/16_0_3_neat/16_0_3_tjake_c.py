import random, math
random.seed()
randint = random.randint

P = 10**7
prime = [1] * (P+1)
div = [1] * (P+1)
prime[0] = prime[1] = 0
primes = []
for i in xrange(2, int(math.sqrt(P))+1):
    if prime[i]:
        for j in xrange(i*i, P+1, i):
            prime[j] = 0
            div[j] = i
        primes.append(i)

def make(l):
    return "1" + ''.join(map(str, [randint(0, 1) for i in xrange(l-2)])) + "1"

def prime_calc(d):
    if d <= P:
        return div[d]
    for p in primes:
        if d % p == 0:
            return p
    return 1

for t in xrange(input()):
    print "Case #%d:"%(t+1)
    n, j = map(int, raw_input().split())

    count = 0
    used = set()
    while count < j:
        s = make(n)
        if s in used:
            continue
        ok = 1
        res = []
        for i in xrange(2, 11):
            d = int(s, i)
            r = prime_calc(d)
            if r==1:
                ok = 0
                break
            res.append(r)
        if ok:
            print s, ' '.join(map(str, res))
            count += 1
        used.add(s)
