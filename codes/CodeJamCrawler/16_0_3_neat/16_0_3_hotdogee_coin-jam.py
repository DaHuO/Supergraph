#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
from math import sqrt

# http://code.activestate.com/recipes/117119-sieve-of-eratosthenes/
def primes():
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = 2 * q # use here 2 * q
            yield q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p

def possible_jamcoins(n):
    i = 0
    fmt = '1{{0:0{0}b}}1'.format(n - 2)
    while True:
        yield fmt.format(i)
        i += 1
        
def int_bases(binary_str, base_start, base_end):
    for b in xrange(base_start, base_end+1):
        yield int(binary_str, b)

def solve(n, j):
    """speed optimization key: just check a few primes then move on
    """
    out = ''
    prime_n = list(itertools.islice(primes(), 100)) # just check n primes
    for pj in possible_jamcoins(n):
        if j == 0: break
        divisors = []
        for inter in int_bases(pj, 2, 10):
            divisor = 0
            sr = int(sqrt(inter)) + 1
            for p in prime_n:
                if p > sr: break
                if inter % p == 0:
                    divisor = p
                    break
            if divisor == 0:
                break
            else:
                divisors.append(str(divisor))
        if len(divisors) != 9:
            continue
        out += '{0} {1}\n'.format(pj, ' '.join(divisors))
        j -= 1
    return out

if __name__ == "__main__":
	for case in xrange(1, 1+input()):
		print "Case #{0}:\n{1}".format(case, solve(*[int(x) for x in raw_input().strip().split()])),