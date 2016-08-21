import sys
from fractions import gcd


primes = [
    2,
     3,
     5,
     7,
     11,
     13,
     17,
     19,
     23,
     29,
     31,
     37,
     41,
     43,
     47,
     53,
     59,
     61,
     67,
     71,
     73,
     79,
     83,
     89,
     97,
     101,
     103,
     107,
     109,
     113,
     127,
     131,
     137,
     139,
     149,
     151,
     157,
     163,
     167,
     173,
     179,
     181,
     191,
     193,
     197,
     199,
     211,
     223,
     227,
     229,
     233,
     239,
     241,
     251,
     257,
     263,
     269,
     271,
     277,
     281,
     283,
     293,
     307,
     311,
     313,
     317,
     331,
     337,
     347,
     349,
     353,
     359,
     367,
     373,
     379,
     383,
     389,
     397,
     401,
     409,
     419,
     421,
     431,
     433,
     439,
     443,
     449,
     457,
     461,
     463,
     467,
     479,
     487,
     491,
     499,
     503,
     509,
     521,
     523,
     541,
 ]

def factor(n, b):
    a = 2
    for j in xrange(2, b):
        a = (a ** j) % n

    d = gcd(a - 1, n);
    if 1 < d < n:
        return d
    else:
        return -1


def factor_rho(n, x_1, limit=30):
    x = x_1;
    xp = (x ** 2 + 1) % n
    p = gcd(x - xp,n)

    while p == 1 and limit > 0:
        x = (x ** 2 + 1) % n
        xp = (xp ** 2 + 1) % n
        xp = (xp ** 2 + 1) % n
        p = gcd(x - xp, n)
        limit -= 100

    if p == n or p == 1:
        return -1
    else:
        return p

def solve(N, J):
    base = 2 ** (N - 1) + 1
    for i in xrange(2 ** (N - 2)):
    # for i in xrange(2 ** (N - 2) - 1, 0, -1):
        j = bin(base + i * 2)[2:]
        divs = []
        bad = False
        for s in xrange(2, 10 + 1):
            num = int(j, s)
            # print 'factor', num
            # sys.stdout.flush()
            for k in primes:
                div = factor_rho(num, k)
                # div = factor(num, k)
                if div !=- 1:
                    break
            if div == -1 or num % div != 0:
                bad = True
                break
            divs.append(div)
        if not bad:
            if J > 0:
                J -= 1
                yield j, divs


tests_count = int(raw_input())
for i in xrange(1, tests_count + 1):
    N, J = map(int, raw_input().split())
    print 'Case #{0}:'.format(i)
    for number, divs in solve(N, J):
        print number, ' '.join(map(str, divs))
        sys.stdout.flush()
