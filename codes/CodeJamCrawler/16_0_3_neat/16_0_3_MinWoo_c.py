
import sys
#sys.stdin = open('c.in', 'r')

PMAX = 1 << 20
is_prime = [1 for _ in xrange(PMAX)]
primes = [2]
for i in xrange(4, PMAX, 2):
    is_prime[i] = 0
for i in xrange(3, PMAX, 2):
    if is_prime[i]:
        for j in xrange(i*2, PMAX, i):
            is_prime[j] = 0
        primes.append(i)

def convert(n, base):
    res = 0
    b, i = 1, 0
    while n > 0:
        res += b if n & 1 else 0
        n >>= 1
        b *= base
    return res

def jamcoin(n): # base10
    for p in primes:
        if p * p > n: break
        if n % p == 0:
            return p
    return -1


T = int(sys.stdin.readline())
for tc in xrange(T):
    print 'Case #%d:' % (tc + 1)
    N, J = map(int, sys.stdin.readline().split())
    K = N - 2
    for m in xrange(1 << K):
        if J == 0: break
        n = (1 << (N - 1)) + (m << 1) + 1
        t = []
        for b in xrange(2, 11):
            bn = convert(n, b)
            z = jamcoin(bn)
            if z == -1:
                break
            t.append(z)
        if len(t) == 9:
            print bin(n)[2:], ' '.join(map(str, t))
            J -= 1
