#!/usr/bin/env python3

import sys
import numpy
import pyprimes


filename = sys.argv[1]
num_cases = 0


def get_factors(num_str):
    factors = []
    for i in range(2, 11):
        num = int(num_str, i)
        factors.append(str(pyprimes.factors(num)[0]))
    return factors

def is_any_prime(num_str):
    for i in range(2, 11):
        num = int(num_str, i)
        if pyprimes.isprime(num):
            return True
    return False

def create_jamcoin_and_divisors(line):
    length = int(line.split()[0])
    count = int(line.split()[1])

    jamcoins = []

    jamcoin = ['1']
    for i in range(length - 2):
        jamcoin.append('0')
    jamcoin.append('1')
    jamcoin = int("".join(jamcoin), 2)

    while len(jamcoins) < count and len(str(numpy.base_repr(jamcoin, 2))) <= length:
        if not is_any_prime(str(numpy.base_repr(jamcoin, 2))):
            factors = get_factors(str(numpy.base_repr(jamcoin, 2)))
            jamcoins.append((str(jamcoin), factors))
        jamcoin = jamcoin + 2

    return jamcoins

with open(filename, 'r') as f:
    num_cases = int(f.readline().strip())
    for i in range(1, num_cases + 1):
        results = create_jamcoin_and_divisors(f.readline().strip())
        print("Case #%d:" % (i))
        for result in results:
            print("%s %s" % (numpy.base_repr(int(result[0]), 2), " ".join(result[1])))

