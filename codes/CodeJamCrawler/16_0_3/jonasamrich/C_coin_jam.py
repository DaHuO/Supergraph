"""Code jam Coin Jam."""

import os
import fileinput
from time import time
import pickle
from itertools import product


def eratosthenes(n):
    """Sieve of eratosthenes."""
    sieve = [True] * n
    for i, is_prime in enumerate(sieve):
        if is_prime:
            yield i
            if i > 1:
                for j in range(i*i, n, i):
                    sieve[j] = False


def get_factor(x, primes):
    """Get some factor of x."""
    for p in primes:
        if x % p == 0:
            return p
        if p >= x:
            return None

# Get some primes
pN = 1000000
filename = 'primes_{}.pickle'.format(pN)

if not os.path.isfile(filename):
    t0 = time()
    with open(filename, 'wb') as f:
        pickle.dump(list(eratosthenes(pN))[2:], f, pickle.HIGHEST_PROTOCOL)
    print('elapsed {}'.format(time() - t0))

with open(filename, 'rb') as f:
    primes = pickle.load(f)
    primes_set = set(primes)
# Compute
[T], [N, J] = map(str.split, (map(str.strip, fileinput.input())))
T, N, J = map(int, [T, N, J])

n_coins = 0

print('Case #1:')

for coin in product(['0', '1'], repeat=N-2):
    coin = '1' + ''.join(coin) + '1'
    is_prime = False
    for base in range(2, 11):
        x = int(coin, base)
        if x in primes_set:
            is_prime = True
            break

    if is_prime:
        continue

    string = coin
    is_hard = False

    for base in range(2, 11):
        x = int(coin, base)
        factor = get_factor(x, primes)

        if factor is None:
            is_hard = True
            break

        string += ' ' + str(factor)

    if is_hard:
        continue

    print(string)
    n_coins += 1
    if n_coins == J:
        break
