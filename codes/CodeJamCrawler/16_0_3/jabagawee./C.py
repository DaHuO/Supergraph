#! /usr/bin/env python


def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True  # n is definitely composite


def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s)
                       for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s)
                       for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])

_known_primes = [2, 3]
_known_primes += [x for x in xrange(5, 2**16, 2) if is_prime(x)]

N = 32
J = 500


def check_jamcoin(number):
    binary_representation = bin(number)[2:]
    for base in range(2, 11):
        basary_representation = int(binary_representation, base)
        if is_prime(basary_representation):
            return False
    return True

jamcoins = []

for odd_number in xrange(2**(N-1)+1, 2**N, 2):
    if check_jamcoin(odd_number):
        jamcoins.append(odd_number)
    if len(jamcoins) == 10000:
        break


def nontrivial_divisor(n):
    for prime in _known_primes:
        if n % prime == 0:
            return prime

print 'Case #1:'
count = 0
for jamcoin in jamcoins:
    answer = [bin(jamcoin)[2:]]
    for i in range(2, 11):
        alternate = int(bin(jamcoin)[2:], i)
        answer.append(str(nontrivial_divisor(alternate)))
    if 'None' not in answer:
        print ' '.join(answer)
        count += 1
    if count == J:
        break
