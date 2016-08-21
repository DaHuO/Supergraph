#! /usr/bin/env python3
#-*- coding: utf8 -*-
import sys
from math import sqrt, ceil


def isCoinjam(coin):
    out = coin
    for base in range(2, 11):
        value = int(coin, base)
        divisor = getDivisor(value)
        if (divisor == 1):
            print(str(value) + " (" + coin + " in base " + str(base) + ") is prime", file=sys.stderr)
            return False
        out += " " + str(divisor)
    print(out)
    return True

def getDivisor(value):
    for prime in PRIMES:
        if (value % prime == 0):
            return(prime)
    return(1)

def isPrime(value, PRIMES):
    sqrt_value = sqrt(value)
    jj = 1
    prime = PRIMES[jj]
    while (prime < sqrt_value):
        if (value % prime == 0):
            return(False)
        jj += 1
        prime = PRIMES[jj]
    PRIMES.append(value)
    return(True)


# Create an initial list of primes
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]
for ii in range(23, 10000, 2):
    isPrime(ii, PRIMES)
if __name__ == "__main__":
    TT = int(input())
    print("Case #1:")
    NN, JJ = [int(_) for _ in input().split()]
    jfound = 0

    coin_value = 2**(NN-1) + 1
    max_value = 2**NN
    test_coins = list()
    max_it = 10000
    it = 0
    while (coin_value < max_value and it < max_it):
        test_coins.append("{0:b}".format(coin_value))
        coin_value += 2
        it += 1
    ii = 0
    while (jfound < JJ and ii < len(test_coins)):
        if (isCoinjam(test_coins[ii])):
            test_coins.pop(ii)
            jfound += 1
        ii += 1
        if (ii >= len(test_coins)):
            # If we still don't have enough coins, update the primes list and look again
            ii = 0
            last_prime = len(PRIMES)
            for jj in range(PRIMES[-1], 2*PRIMES[-1], 2):
                isPrime(jj, PRIMES)
            PRIMES = PRIMES[(last_prime-1):] # Remove the primes already explored
    print(str(jfound) + " coins found", file=sys.stderr)

