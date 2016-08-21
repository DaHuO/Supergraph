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

for line in lines[1:]:
    casenum += 1
    s = line.strip()

    t = ''
    t += s[0]
    for c in s[1:]:
        if c < t[0]:
            #print 'less ' + c + ' ' + t
            t = t + c
        else:
            #print 'more ' + c + ' ' + t
            t = c + t
    
    print 'case #' + str(casenum) + ": " + t


        
