#!/usr/bin/env python3
"""
Problem C. Coin Jam
CodeJam 2016: Qualification Round
https://code.google.com/codejam/contest/6254486/dashboard#s=p2

How to run:
$ ./coinjam.py < sample.in > sample.out

Validate:
$ diff -s sample.out sample.out.key
Files sample.out and sample.out.key are identical
"""
import json
import time
from itertools import count, islice, product


__author__ = "Tatiana Al-Chueyr"
__email__ = "tatiana.alchueyr@gmail.com"
__date__ = "2016-04-09"
__version__ = "2.0.0"


MAX_PRIME = 10000


def primes_to_n(n):
    """
    Given a number n >= 6, return an array of primes 2 <= p < n.
    """
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]


PRIMES = primes_to_n(MAX_PRIME)


def create_possible_jamcoin_combinations(size):
    """
    Generator of possible jamcoins, given the expected size.
    It respects the two first conditions of jamcoins:
    - Every digit is either 0 or 1.
    - The first digit is 1 and the last digit is 1.
    The output is a jaimcoin string.
    """
    assert size > 1

    if size == 2:
        yield "11"
    else:
        size -= 2
        for combination in product(range(2), repeat=size):
            combination = "".join([str(char) for char in combination])
            jamcoin = "1{}1".format(combination)
            yield jamcoin


def is_prime(number):
    """
    Checks if a number is a prime < MAX_PRIME.
    """
    return number in PRIMES


def is_composite(n):
    """
    Checks if number is a composite number (not prime).

    If it returns 0, it may be one of the following:
    - it is a prime number
    - it has no prime divisor <= MAX_PRIME

    Otherwise, return a nontrivial divisor: positive integer other than 1 or
    the number itself.
    """
    assert n > 1
    # most expensive!!!!
    if is_prime(n):
        return 0
    candidate_divisors = [p for p in PRIMES if p <= int(n**0.5)]
    for number in candidate_divisors:
        if not n % number:
            return number
    return 0


def is_composite_in_all_bases(string):
    """
    Checks if integer represented in the string is a composite number in all
    the bases between 2 and 10, inclusive.

    If it is prime in any base, return [] (empty list)
    Otherwise, return a list containing one non-trivial divisor for each base
    """
    divisors = []
    for base in range(2, 11):
        number = int(string, base)
        base_divisor = is_composite(number)
        if not base_divisor:
            return []
        else:
            divisors.append(base_divisor)
    return divisors


def produce_jamcoins(n, j):
    """
    Return a list containing j jamcoins of size n.
        Each jamcoin is a tuple of 10 items:
        <jamcoin> <base-2-divisor> <base-3-divisor> ... <base-10-divisor>
    """
    found = 0
    response_list = []
    init = time.time()
    for possible_jamcoin in create_possible_jamcoin_combinations(n):
        if found == j:
            break
        else:
            response = is_composite_in_all_bases(possible_jamcoin)
            if response:
                response.insert(0, possible_jamcoin)
                response_list.append(response)
                found += 1
    return response_list


if __name__ == "__main__":
    TOTAL = int(input())
    for i in range(1, TOTAL + 1):
        print("Case #{}:".format(i))
        n, j = [int(s) for s in input().split(" ")]
        for response in produce_jamcoins(n, j):
            print(" ".join([str(i) for i in response]))
