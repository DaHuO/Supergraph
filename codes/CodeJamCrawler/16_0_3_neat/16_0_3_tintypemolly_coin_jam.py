#!/usr/bin/python
#  L3-L77 is copied from https://rosettacode.org/wiki/Prime_decomposition#Python
from __future__ import print_function

from itertools import islice, cycle, count

try:
    from itertools import compress
except ImportError:
    def compress(data, selectors):
        """compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F"""
        return (d for d, s in zip(data, selectors) if s)


def is_prime(n):
    return list(zip((True, False), decompose(n)))[-1][0]


class IsPrimeCached(dict):
    def __missing__(self, n):
        r = is_prime(n)
        self[n] = r
        return r


is_prime_cached = IsPrimeCached()


def croft():
    """Yield prime integers using the Croft Spiral sieve.

    This is a variant of wheel factorisation modulo 30.
    """
    # Copied from:
    #   https://code.google.com/p/pyprimes/source/browse/src/pyprimes.py
    # Implementation is based on erat3 from here:
    #   http://stackoverflow.com/q/2211990
    # and this website:
    #   http://www.primesdemystified.com/
    # Memory usage increases roughly linearly with the number of primes seen.
    # dict ``roots`` stores an entry x:p for every prime p.
    for p in (2, 3, 5):
        yield p
    roots = {9: 3, 25: 5}  # Map d**2 -> d.
    primeroots = frozenset((1, 7, 11, 13, 17, 19, 23, 29))
    selectors = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)
    for q in compress(
            # Iterate over prime candidates 7, 9, 11, 13, ...
            islice(count(7), 0, None, 2),
            # Mask out those that can't possibly be prime.
            cycle(selectors)
    ):
        # Using dict membership testing instead of pop gives a
        # 5-10% speedup over the first three million primes.
        if q in roots:
            p = roots[q]
            del roots[q]
            x = q + 2 * p
            while x in roots or (x % 30) not in primeroots:
                x += 2 * p
            roots[x] = p
        else:
            roots[q * q] = q
            yield q


primes = croft


def decompose(n):
    for p in primes():
        if p * p > n: break
        while n % p == 0:
            yield p
            n //= p
    if n > 1:
        yield n


def get_jamcoin_test(string):
    nontrivial_divisor_list = list()
    for base in range(2, 11):
        nontrivial_divisor = smallest_nontrivial_divisor(string, base)
        if nontrivial_divisor is None:
            return False, None
        nontrivial_divisor_list.append(str(nontrivial_divisor))
    return True, nontrivial_divisor_list


def smallest_nontrivial_divisor(string, base):
    number = get_int_with_base(string, base)
    generator = decompose(number)
    factor = generator.next()
    if factor == number:
        return None
    else:
        return factor


def get_int_with_base(string, base):
    raw_value = int(string)
    if base == 10:
        return raw_value
    power = 0
    value = 0
    while raw_value > 0:
        value += (raw_value % 10) * (base ** power)
        power += 1
        raw_value /= 10
    return value


def generate_string(length):
    mid_length = length - 2
    for i in range(2 ** mid_length):
        yield '1%s1' % ('{0:0%db}' % mid_length).format(i)


def main():
    with open('C-small-attempt0.in') as input_file, open('C-small-attempt0.out', 'w') as output_file:
        # throw out first line
        input_file.readline()
        line = input_file.readline().strip()
        n, j = line.split(' ')
        n, j = int(n), int(j)
        count = 0
        output_file.write('Case #1:\n')
        for string in generate_string(n):
            is_jamcoin, nontrivial_divisors = get_jamcoin_test(string)
            if is_jamcoin:
                output_file.write('%s %s\n' % (string, ' '.join(nontrivial_divisors)))
                output_file.flush()
                count += 1
                if count == j:
                    break


if __name__ == '__main__':
    main()
