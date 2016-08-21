#!/usr/bin/env python3

from itertools import product


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


# Use the precalculated table
def calculate_divisor(n, prime_table):
    for i in prime_table:
        if n % i == 0 and n != i:
            return i
    # Not found, good luck with the next one
    return None


def jamcoins(n, j):
    prime_table = [i for i in range(2, 1000 + 1) if is_prime(i)]
    res_n = 0
    res = []
    for t in product('01', repeat=n - 2):
        possible_jamcoin = "".join(['1'] + list(t) + ['1'])
        divisors = []
        for base in range(2, 10 + 1):
            tentative_number = int(possible_jamcoin, base=base)
            divisor = calculate_divisor(tentative_number, prime_table)
            if divisor is None:
                break
            else:
                divisors.append(divisor)
        if len(divisors) == 9:
            # A jamcoin!
            res.append([possible_jamcoin] + divisors)
            res_n += 1
            if res_n == j:
                break
    return res

#jamcoins(6, 3)

t = int(input())
for i in range(1, t+1):
    n, j = str(input()).split(" ")
    r = jamcoins(int(n), int(j))
    print("Case #{}:".format(i))
    for row in r:
        print(" ".join((str(e) for e in row)))
