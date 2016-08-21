import random
import math

MIN_BASE = 2
MAX_BASE = 10
MAX_POW = 32
N_FACTORS = MAX_BASE - MIN_BASE + 1

power = [[1 for _ in xrange(MAX_POW)] for _ in xrange(MAX_BASE + 1)]
for base in xrange(MIN_BASE, MAX_BASE + 1):
    for exp in xrange(1, MAX_POW):
        power[base][exp] = power[base][exp - 1] * base


some_primes = [2]
MAX_PRIME = 1 << (MAX_POW / 2)
is_prime = [True for _ in xrange(MAX_PRIME)]
for n in xrange(3, MAX_PRIME, 2):
    if is_prime[n]:
        some_primes.append(n)
        for f in xrange(n, MAX_PRIME / n + 1):
            is_prime[n * f] = False


def find_factor(n):
    v = math.sqrt(n)
    for p in some_primes:
        if p > v:
            return 0  # haven't found a factor
        if n % p == 0:
            return p


def find(N, J):
    found = 0
    already_found = set()

    while found < J:
        numbers = [0 for _ in xrange(MIN_BASE, MAX_BASE + 1)]
        bits = ''

        x = random.randint(0, (1 << (N-2)) - 1)
        for i in xrange(N-2):
            if x & (1 << i):
                bits += '1'
                numbers = [n + power[b][i] for b, n in enumerate(numbers, MIN_BASE)]
            else:
                bits += '0'

        bits = '1' + bits[::-1] + '1'
        numbers = [n * b + power[b][0] for b, n in enumerate(numbers, MIN_BASE)]
        numbers = [n + power[b][N-1] for b, n in enumerate(numbers, MIN_BASE)]

        if bits not in already_found:
            factors = []
            for n in numbers:
                f = find_factor(n)
                if not f:
                    break
                factors.append(f)

            if len(factors) == N_FACTORS:
                found += 1
                already_found.add(bits)
                print bits, ' '.join([str(f) for f in factors])


raw_input()
N, J = [int(x) for x in raw_input().split(' ')]
print "Case #1:"
find(N, J)
