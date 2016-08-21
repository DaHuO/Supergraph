#!/usr/bin/env python

import sys
from itertools import product


def bases(s):
    return [int(s, base) for base in range(2, 10+1)]


def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2, 3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]


primes = rwh_primes2(1000000)


def check(x):
    for p in primes:
        if x <= p:
            return False
        if x % p == 0:
            return p
    return False


def omg(x):
    y = '1{}1'.format(''.join(x))
    bs = bases(y)
    n = bs[-1]
    factors = [check(b) for b in bases(y)]
    if all(factors):
        print('{} {}'.format(y, ' '.join(map(str, factors))))
        return True
    return False


def read(f):
    T = int(f.readline())
    assert T == 1
    inputs = []
    for line in f:
        N, J = line.split()
        inputs.append((int(N), int(J)))
    return inputs


def output(p):
    y = '1{}1'.format(''.join(p))
    


def main():
    inputs = read(sys.stdin)
    for i, (N, J) in enumerate(inputs, start=1):
        print('Case #{}:'.format(i))
        j = 0
        for p in product('01', repeat=N-2):
            if omg(p):
                j += 1
                if j >= J:
                    break


if __name__ == '__main__':
    main()
    
