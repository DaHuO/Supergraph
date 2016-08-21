#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import print_function
import math
import argparse

def sieve(n):
    discovered = [2]
    for i in xrange(3, n+1):
        is_prime = True
        for p in discovered:
            if i % p == 0:
                is_prime = False
        if is_prime:
            discovered += [i]
    return discovered

# def sieve(n):
#     not_prime = []
#     prime = []
#     for i in xrange(2, n+1):
#         if i not in not_prime:
#             prime.append(i)
#             for j in xrange(i*i, n+1, i):
#                 not_prime.append(j)
#     return prime

def split_by_length(primes):
    res = {}
    for p in primes:
        l = int(math.ceil(math.log(p, 2)))
        res.setdefault(l, []).append(p)
    return res

# def is_prime(num):
#     if num == 2:
#         return True
#     if not num & 1:
#         return False
#     return pow(2, num-1, num) == 1

def is_prime(num, primes):
    for p in primes:
        if num % p == 0:
            return p

def construct_number(n, primes_by_length):
    import random
    seen = set()
    if n <= 16:
        for x in range(2, n//2 + 1):
            y = n - x
        for p1 in primes_by_length[x]:
            for p2 in primes_by_length[y]:
                candidate = format(p1 * p2, 'b')
                if candidate[0] == '1' and candidate[-1] == '1' and len(candidate) == n and candidate not in seen:
                    seen.add(candidate)
                    yield candidate
    else:
        # take numbers with 16 bits
        for p in primes_by_length[16]:
            for c in construct_number(n - 16, primes_by_length):
                c = int(c, 2)
                candidate = format(c * p, 'b')
                if candidate[0] == '1' and candidate[-1] == '1' and len(candidate) == n and candidate not in seen:
                    seen.add(candidate)
                    yield candidate

def solve(n, j, primes, primes_by_length):
    values = []
    # let's get all primes that are of length j
    for candidate in construct_number(n, primes_by_length):
        row = [candidate]
        for b in range(2, 10 + 1):
            v = int(candidate, b)
            d = is_prime(v, primes)
            if d:
                row += [d]
        if len(row) == 10:
            values += [row]
            if len(values) == j:
                return values

def check(row):
    for b in range(2, 10 + 1):
        v = int(row[0], b)
        d = row[b-1]
        if v % d > 0:
            raise

if __name__ == '__main__':
    import sys

    primes = sieve(2**16)
    primes_by_length = split_by_length(primes)

    print ("Precomputation done, continue?")
    raw_input()
    print ("Continuing...")

    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=str, default='stdin')
    parser.add_argument('--dst', type=str, default='stdout')

    stream2name = {
        'stdin' : sys.stdin,
        'stdout': sys.stdout,
        'stderr': sys.stderr,
    }

    args = parser.parse_args()
    target_ro = stream2name.get(args.src)
    if not target_ro:
        target_ro = open(args.src, 'ro')
    target_w = stream2name.get(args.dst)
    if not target_w:
        target_w = open(args.dst, 'w')

    with target_ro as src:
        with target_w as dst:
            t = int(src.readline())
            for i in range(t):
                n, j = map(int, src.readline().strip().split())
                res = solve(n, j, primes, primes_by_length)
                print("Case #%s:" % (i+1), file=dst)
                for row in res:
                    print(" ".join([str(x) for x in row]), file=dst)
                    check(row)


    """
    Problem

        A jamcoin is a string of N ≥ 2 digits with the following properties:

        Every digit is either 0 or 1.
        The first digit is 1 and the last digit is 1.
        If you interpret the string in any base between 2 and 10, inclusive, the resulting number is not prime.
        Not every string of 0s and 1s is a jamcoin. For example, 101 is not a jamcoin; its interpretation in base 2 is 5, which is prime. But the string 1001 is a jamcoin: in bases 2 through 10, its interpretation is 9, 28, 65, 126, 217, 344, 513, 730, and 1001, respectively, and none of those is prime.

        We hear that there may be communities that use jamcoins as a form of currency. When sending someone a jamcoin, it is polite to prove that the jamcoin is legitimate by including a nontrivial divisor of that jamcoin's interpretation in each base from 2 to 10. (A nontrivial divisor for a positive integer K is some positive integer other than 1 or K that evenly divides K.) For convenience, these divisors must be expressed in base 10.

        For example, for the jamcoin 1001 mentioned above, a possible set of nontrivial divisors for the base 2 through 10 interpretations of the jamcoin would be: 3, 7, 5, 6, 31, 8, 27, 5, and 77, respectively.

        Can you produce J different jamcoins of length N, along with proof that they are legitimate?

        Input

        The first line of the input gives the number of test cases, T. T test cases follow; each consists of one line with two integers N and J.

        Output

        For each test case, output J+1 lines. The first line must consist of only Case #x:, where x is the test case number (starting from 1). Each of the last J lines must consist of a jamcoin of length N followed by nine integers. The i-th of those nine integers (counting starting from 1) must be a nontrivial divisor of the jamcoin when the jamcoin is interpreted in base i+1.

        All of these jamcoins must be different. You cannot submit the same jamcoin in two different lines, even if you use a different set of divisors each time.

        Limits

        T = 1. (There will be only one test case.)
        It is guaranteed that at least J distinct jamcoins of length N exist.

        Small dataset

        N = 16.
        J = 50.
        Large dataset

        N = 32.
        J = 500.
        Note that, unusually for a Code Jam problem, you already know the exact contents of each input file. For example, the Small dataset's input file will always be exactly these two lines:

        1
        16 50
        So, you can consider doing some computation before actually downloading an input file and starting the clock.

        Sample


        Input

        1
        6 3

        Output

        Case #1:
        100011 5 13 147 31 43 1121 73 77 629
        111111 21 26 105 1302 217 1032 513 13286 10101
        111001 3 88 5 1938 7 208 3 20 11

        In this sample case, we have used very small values of N and J for ease of explanation. Note that this sample case would not appear in either the Small or Large datasets.

        This is only one of multiple valid solutions. Other sets of jamcoins could have been used, and there are many other possible sets of nontrivial base 10 divisors. Some notes:

        110111 could not have been included in the output because, for example, it is 337 if interpreted in base 3 (1*243 + 1*81 + 0*27 + 1*9 + 1*3 + 1*1), and 337 is prime.
        010101 could not have been included in the output even though 10101 is a jamcoin, because jamcoins begin with 1.
        101010 could not have been included in the output, because jamcoins end with 1.
        110011 is another jamcoin that could have also been used in the output, but could not have been added to the end of this output, since the output must contain exactly J examples.
        For the first jamcoin in the sample output, the first number after 100011 could not have been either 1 or 35, because those are trivial divisors of 35 (100011 in base 2).
"""