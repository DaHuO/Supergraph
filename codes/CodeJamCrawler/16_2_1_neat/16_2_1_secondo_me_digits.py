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

dletters = [
    'ZERO',
    'ONE',
    'TWO',
    'THREE',
    'FOUR',
    'FIVE',
    'SIX',
    'SEVEN',
    'EIGHT',
    'NINE']   

uniq='ZOWHRFXVGI'
allletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for line in lines[1:]:
    casenum += 1
    pnum = line.strip()

    counts = {}
    for l in allletters:
        counts[l] = pnum.count(l)

    dct = [0]*10

    for d in [0,2,6,8,3,4,5,1,7,9]:
        dct[d] = counts[uniq[d]]
        for l in dletters[d]:
            counts[l] -= dct[d]

    ans=''
    for d in range(10):
        ans += str(d)*dct[d]

    print 'case #' + str(casenum) + ': ' + ans


        
