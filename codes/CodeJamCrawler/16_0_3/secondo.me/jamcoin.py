import sys
from fractions import gcd
import numpy as np

def primesfrom3to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns a array of primes, p < n """
    assert n>=2
    sieve = np.ones(n/2, dtype=np.bool)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = False
    return np.r_[2*np.nonzero(sieve)[0][1::]+1]    

primes=primesfrom3to(100)
prod_primes = 1L
for p in primes:
    prod_primes *= long(p)

def nontrivial_divisor(n):
    d = gcd(n,prod_primes)

    if d == n:
        for p in primes:
            if d%p == 0:
                d=p
                break

    return d


lines = open(sys.argv[1]).readlines()

T = int(lines[0])

casenum = 0

for line in lines[1:]:
    casenum += 1
    vals = line.split()
    N = int(vals[0])
    J = int(vals[1])

    print 'case #' + str(casenum) + ":"


    start = 2**(N-1)+1
    stop  = 2**(N)

    count = 0

    c = start

    while(1):
        c += 2

        binstr = '{0:b}'.format(c)

        divisors = []

        for base in range(2,11):
            num_in_base = long(binstr,base)
            d = nontrivial_divisor(num_in_base)

            if d == 1:
                break

            divisors.append(str(d))

        if len(divisors) < 9:
            continue

        print binstr + ' ' + ' '.join(divisors)
        count += 1

        if (count >= J):
            break
        
