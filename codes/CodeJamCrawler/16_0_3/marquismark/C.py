#!/usr/bin/env python

TEST="""1
6 3"""
#raw_input = iter(TEST.splitlines()).next

def primes(N=1000000):
    sieve = [1]*(N+2)
    sieve[0] = 0
    sieve[1] = 0
    primes = []
    for i,prime in enumerate(sieve):
        if prime:
            primes.append(i)
            n = i+i
            while n < len(sieve):
                sieve[n] = 0
                n += i
    return primes 

PRIMES = primes()

def rebase(N, base):
    """ Interpret N in new base. 9,10 ==> 1001 """
    u = 0
    R = 0
    while N:
        if N%2 == 1:
            R += base**u     
            N -= 1
        N /= 2
        u += 1
    return R

def divisor(i):
    for p in PRIMES:
        if i%p == 0:
            return p
        if p*p > i:
            return False

def get_divisors(I):
    r = []
    for i in I:
        d = divisor(i)
        if d:
            r.append(d)
        else:
            return False
    return r

def solve(N, J):
    results = []
    i = 2**(N-1) + 1
    while len(results) != J:
        interps = [rebase(i, b) for b in range(2,11)]
        divisors = get_divisors(interps)
        if divisors:
            jamcoin = "%s %s" % (bin(i)[2:], 
                             " ".join(str(s) for s in divisors))
            results.append(jamcoin)
        i += 2
    return results

T = int(raw_input())
for case in range(1,T+1):
    N,J = map(int, raw_input().strip().split())
    print("Case #%s:" % case)
    for result in solve(N,J):
        print(result)
