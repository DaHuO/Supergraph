import math
import itertools


def is_prime(n):
    if (n % 2 == 0):
        return False, 2
    m = int(math.sqrt(n))
    for i in xrange(3, m + 1, 2):
        if n % i == 0:
            return False, i
    return True, None


def to_base(jamcoin, base):
    jamcoin_int = 0
    power = 1
    for i in xrange(len(jamcoin) - 1, -1, -1):
        if jamcoin[i] == 1:
            jamcoin_int += power
        power *= base
    return jamcoin_int


def is_legitimate(jamcoin):
    if jamcoin[0] == 0 or jamcoin[-1] == 0:
        return False, None
    divisors = []
    for base in xrange(2, 11):
        jamcoin_int = to_base(jamcoin, base)
        prime, divisor = is_prime(jamcoin_int)
        if not prime:
            divisors.append(divisor)
        else:
            return False, None
    return True, divisors


def produce_jamcoins(n, j):
    res = []
    if j == 0:
        return res
    jamcoins = itertools.product([0, 1], repeat=n)
    for jamcoin in jamcoins:
        legitimate, divisors = is_legitimate(jamcoin)
        if legitimate:
            res.append((jamcoin, divisors))
            if len(res) == j:
                return res
    return res


t = int(raw_input())
for i in xrange(1, t + 1):
    n, j = [int(s) for s in raw_input().split(" ")]
    res = produce_jamcoins(n, j)
    print "Case #{}:".format(i)
    for jamcoin, divisors in res:
        print "{} {}".format(
            "".join(str(digit) for digit in jamcoin),
            " ".join(str(divisor) for divisor in divisors)
        )
