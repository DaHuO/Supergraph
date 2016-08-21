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
    return np.r_[2,2*np.nonzero(sieve)[0][1::]+1]    

primes=primesfrom3to(100)
prod_primes = 1L
for p in primes:
    prod_primes *= long(p)

def nontrivial_divisor(n):
    d = 1
    for p in primes:
        if n%p == 0:
            d=p
            break

    return d


lines = open(sys.argv[1]).readlines()

T = int(lines[0])

casenum = 0

pos = 1
for casenum in xrange(1,T+1):
    N = int(lines[pos])

    pos += 1

    count = {}
    for i in xrange(2*N-1):
        tmp = lines[pos].split()
        for v in tmp:
            if v in count:
                count[v] ^= 1
            else:
                count[v] = 1
        pos += 1

    print 'case #' + str(casenum) + ": ",

    vals = []
    for x in sorted(count.keys()):
        if count[x]:
            vals.append(int(x))

    print ' '.join([str(x) for x in sorted(vals)])
    




        
