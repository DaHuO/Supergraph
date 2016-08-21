import math
from math import sqrt
from itertools import count, islice


def is_prime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True


def divisor_generator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def is_jamcoin(j):
    for x in xrange(2,11,1):
        if is_prime(int(str(j), x)):
            return False
    return True


def find_jamcoin(n, found = []):
    s, t = int("1{0}1".format('0' * (n - 2))), int("1{0}1".format('1' * (n - 2)))
    for x in xrange(s, t, 1):
        if len([y for y in list(set(str(x))) if int(y) > 1]) == 0 and str(x)[len(str(x)) - 1] == "1":
            if is_jamcoin(x) and x not in found:
                return x

def check_divisor(d, c):
    if d == 1:
        return False

    for x in xrange(2,11,1):
        if d == int(str(c), x):
            return False
    return True


def start():
    t = 1
    # t = int(raw_input().strip())
    # n, j = [int(x) for x in raw_input("Enter two numbers here: ").split()]
    n, j = 16, 50

    found = []

    print "Case #1:"
    for test in range(j):
        coin = find_jamcoin(n, found)
        found.append(coin)
        divisors = []
        for x in xrange(2,11,1):
            l = list(divisor_generator(int(str(coin), x)))
            for y in reversed(l):
                if check_divisor(y, coin):
                    divisors.append(y)
                    break
        print coin, ''.join([''.join(str(x) + " ") for x in divisors])


