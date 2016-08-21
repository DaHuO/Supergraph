#!/usr/bin/env python

import itertools
import math
import sys

class IsPrime(Exception):
    pass

T = int(raw_input().strip())

assert T == 1

def find_divisor(num):
    for divisor in xrange(2, int(math.sqrt(num))+1):
        if num % divisor == 0:
            return divisor
    raise IsPrime

def test_jamcoin(coinstr):
    divisors = []
    for base in xrange(2, 11):
        num = int(coinstr, base)
        try:
            divisors.append(str(find_divisor(num)))
        except IsPrime:
            return False
    return divisors
def find_jamcoins(N):
    for i in xrange(2**(N-1) + 1, 2**N, 2):
        coin = bin(i)[2:]
        divisors = test_jamcoin(coin)
        if divisors:
            yield coin, divisors

assert test_jamcoin('110111') == False
assert test_jamcoin('101') == False
assert test_jamcoin('100011') != False
assert test_jamcoin('1001') != False

for i in range(1, T+1):
    print ("Case #%d:" % i)
    N, J = [int(x) for x in raw_input().strip().split()]
    for coin, divisors in itertools.islice(find_jamcoins(N), 0, J):
        print coin, ' '.join(divisors)
        sys.stdout.flush()
