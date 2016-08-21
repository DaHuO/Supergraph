from math import sqrt, ceil
from itertools import product


def check(x):
    root = sqrt(x)
    for i in primes:
        if i > root:
            return 1
        if x % i == 0:
            return i


def is_prime(x):
    if x in primes2:
        return 1
    return check(x)

file = open("primes.out", "r")
primes = map(int, file.read().split(" "))
primes2 = set(primes)
size = len(primes)

t = int(raw_input())
n, j = map(int, raw_input().split())

limit = int(ceil(sqrt(int("1" * n) + 7)))

count = 0
print "Case #1:"
for item in product("01", repeat = n-2):
    current = "1" + "".join(item) + "1"
    factors = []
    p = True
    for a in xrange(2, 11):
        ans = is_prime(int(current, a))
        if ans == 1:
            p = False
            break
        else:
            factors.append(ans)
    if p:
        print "{} {}".format(current, " ".join(map(str, factors)))
        count += 1
        if count == j:
            break
