#!/usr/bin/env python3
import itertools
import math
import os
import sys
import urllib.request

if not os.path.isfile("primes1.txt"):
    urllib.request.urlretrieve("https://primes.utm.edu/lists/small/millions/primes1.zip",
                               "primes1.zip")
    os.system("unzip primes1.zip")

primes = []
with open("primes1.txt") as f:
    next(f)
    next(f)

    for line in f:
        for prime in line.split():
            primes.append(int(prime))

def parse():
    n_cases = int(sys.stdin.readline())
    cases = [l.strip().split() for l in sys.stdin]

    assert len(cases) == n_cases, cases

    return cases

def divisor(n):
    # print(n, end=" ")
    sqrt_n = math.sqrt(n)
    for p in primes:
        if p > sqrt_n:
            return None
        if n % p == 0:
            return p

def solve(N, J, bases=range(2, 11)):
    numbers = ("1" + "".join(n) + "1" for n in itertools.product("01", repeat=int(N) - 2))

    results = 0
    step = 0

    print("Case #1: ")

    while results < int(J):
        step += 1
        number_s = next(numbers)
        print(step, results, sep = "\t", file=sys.stderr)
        result = [number_s]
        for base in bases:
            n = int(number_s, base)
            d = divisor(n)
            assert d != n
            if d is None:
                break
            else:
                result.append(d)
        else:
            assert len(result) == 10, result
            results += 1
            print(*result)

for i, case in enumerate(parse()):
    solve(*case)
