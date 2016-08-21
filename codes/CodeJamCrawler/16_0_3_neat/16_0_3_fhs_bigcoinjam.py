#!/usr/bin/env python3

import math

def isprime(n):
    if n < 2:
        return n, False
    if n == 2:
        return n, True
    if n%2 == 0:
        return n, False
    s = math.sqrt(n)
    i = 3
    while i <= s:
        if n%i == 0:
            return i, False
        i += 2
    return n, True

def basen(n, base):
    r = 0
    b = 1
    while n > 0:
        r += (n&1) * b
        b *= base
        n >>= 1
    return r

primes = [x for x in range(3, 1000) if isprime(x)[1]]

def iscoinjam(n):
    divisors = [None]*11
    for base in range(2, 11):
        bn = n
        if base != 2:
            bn = basen(n, base)

        q = None
        for prime in primes:
            if bn%prime == 0:
                q = prime
                break
        if q is None:
            return None, False
        divisors[base] = q
        #print("base", base, bn, q)
    return divisors, True

def main():
    N = 32
    NCases = 500
    MinCoinJam = (1<<(N-1)) | 1
    MaxCoinJam = (1<<N)-1

    n = 0
    print("Case #1:")
    for i in range(MinCoinJam, MaxCoinJam+1, 2):
        if n >= NCases:
            break
        divisors, ok = iscoinjam(i)
        if ok:
            print(bin(i)[2:], end="")
            for base in range(2, 11):
                print(" %d" % divisors[base], end="")
            print("", flush=True)
            n += 1

if __name__ == '__main__':
    main()
