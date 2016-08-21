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

let='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for casenum in xrange(1,T+1):
    N = int(lines[2*casenum-1])
    vals = lines[2*casenum].split()
    vals = [int(x) for x in vals]

    ans = ''

    M = max(vals)
    while M > 0:
        first = vals.index(M)
        ct = vals.count(M)
        ans += ' ' + let[first]
        vals[first] -= 1
        
        if ct == 2:
            first = vals.index(M)
            ans += let[first]
            vals[first] -= 1
            
        M = max(vals)


    print 'case #' + str(casenum) + ":" + ans

    
        
