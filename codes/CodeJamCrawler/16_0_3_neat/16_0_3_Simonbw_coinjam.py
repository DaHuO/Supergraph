# /usr/bin/env python3

from math import sqrt


def get_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]
PRIMES = get_primes(1000000)
PRIME_SET = set(PRIMES)


def get_factor(n):
    if n in PRIME_SET:
        return None
    for p in PRIMES:
        if n % p == 0:
            return p
    return None


def get_factors(s):
    """Return true if a number is a jam coin"""
    factors = []
    for base in range(2, 11):
        n = int(s, base)
        factor = get_factor(n)
        if factor is None:
            return None
        factors.append(factor)
    return factors


for case_number in range(int(input())):
    print("Case #" + str(case_number + 1) + ":")
    N, J = [int(x) for x in input().split()]

    found = 0
    for i in range(2 ** (N - 2)):
        if found >= J:
            break
        s = '1' + format(i, 'b').zfill(N - 2) + '1'
        factors = get_factors(s)
        if factors is not None:
            found += 1
            print(s, ' '.join(map(str, factors)))
