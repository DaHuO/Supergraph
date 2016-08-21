#!/usr/bin/python3

import sys
import itertools


primes = {}
divisors = {}

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        divisors[n] = n // 2
        return False
    if n % 3 == 0:
        divisors[n] = 3
        return False

    if n in primes:
        return primes[n]

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            divisors[n] = n // i
            primes[n] = False
            return False
        i += w
        w = 6 - w

    primes[n] = True
    return True

def my_gen(digits, need):
    inputs = map(lambda x: "1{}1".format(x),
                 map(lambda x: ''.join(map(str, x)),
                     itertools.product([0, 1], repeat=digits)))

    k = 0
    while True:
        for i in inputs:
            decs =  list(map(lambda x: int(i, x), range(2, 11)))
            if any(map(lambda x: isprime(int(x)), decs)):
                continue
            else:
                if k <= need:
                    key, value = i, " ".join(map(lambda x: str(divisors[x]), decs))
                    yield "{} {}".format(key, value)
                    k += 1
                else:
                    raise StopIteration()

number_of_test_cases = int(sys.stdin.readline())
base, need = map(int, sys.stdin.read().strip().split())
g = my_gen(base - 2, need)
next(g)
print("Case #{}:".format(number_of_test_cases))
for t in g:
    print(t)
