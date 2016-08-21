#!/usr/bin/env python3

import sys, random

N = int(sys.argv[1])
J = int(sys.argv[2])


def make_jamcoins(number, length):
    D = ["0", "1"]
    found = {}

    while len(found) < number:
        s = "".join(random.choice(D) for _ in range(length))
        if s[0] != '1' or s[-1] != '1' or s in found:
            continue

        divisors = is_valid_jamcoin(s)
        if divisors:
            found[s] = divisors

    return found

def get_proper_divisor(n):
    bound = int(n**0.5 + 1)
    for d in range(2, bound+1):
        if n % d == 0:
            return d
    return None

def is_valid_jamcoin(s):
    divisors = []

    for base in range(2, 11):
        n = int(s, base)
        divisor = get_proper_divisor(n)

        if not divisor:
            return False
        else:
            divisors.append(divisor)

    return divisors


coins = make_jamcoins(J, N)
print("Case #1:")
for coin, divisors in coins.items():
    L = [coin] + [str(x) for x in divisors]
    print(" ".join(L))

