import sys
from pyprimes import isprime, factorise
from itertools import islice

LENGTH = 32
NUM_SOLS = 500

N_MAX = 100000

primes_under_max = [n for n in range(2, N_MAX) if isprime(n)]

def get_factor(num):
    for prime in primes_under_max:
        if num % prime == 0:
            return prime
    return None

solutions_found = 0

print("Case #1:")

i = 0
while solutions_found < NUM_SOLS:
    n = 1 + (2 ** (LENGTH - 1)) + (2 * i)
    bin_n = "{:b}".format(n)


    factors = []
    for base in range(2, 11):
        m = int(bin_n, base)

        factor = get_factor(m)

        if factor is None:
            break

        factors.append(factor)

    if len(factors) == 9:
        print("{} {}".format(bin_n, " ".join(map(str, factors))))
        solutions_found += 1
    i += 1
