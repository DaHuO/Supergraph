import itertools

import math


def spf(n):
    if n < 2:
        raise ValueError('{} does not have a prime factorization'.format(n))
    divisor = 2
    while n > 1:
        if not n % divisor:
            return divisor
        divisor += 1
    return divisor


def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(7)
    True
    """
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def check(p):
    """
    >>> check("100011")
    test
    >>> check("101")
    []
    """
    bases = list()
    for b in range(2, 11):
        base = int(p, b)
        if is_prime(base):
            break
        bases.append(spf(base))
    return bases


def calculate(n, j):
    """
    >>> calculate(16, 50)
    test
    """

    returns = list()
    for p in [item for item in itertools.product("10", repeat=n - 2)]:
        if len(returns) == j:
            break
        pStr = "1" + "".join(str(pI) for pI in p) + "1"
        checks = check(pStr)
        if len(checks) == 9:
            returns.append((pStr, checks))

    return returns


t = int(input())
for tI in range(0, t):
    splitInput = str(input()).split(" ")
    print("Case #{}".format(tI + 1))
    for part in calculate(int(splitInput[0]), int(splitInput[1])):
        print("{} {}".format(part[0], " ".join(str(pI) for pI in part[1])))
