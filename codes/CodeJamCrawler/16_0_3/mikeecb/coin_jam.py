from math import sqrt
from itertools import count, islice

def memoize(f):
  class memodict(dict):
      __slots__ = ()
      def __missing__(self, key):
          self[key] = ret = f(key)
          return ret
  return memodict().__getitem__

def prime_or_factor(n):
    if n > 1:
        for i in xrange(2, 20):
            if n % i == 0:
                return (False, i)
    return (True, None)

def generate_possible_coins(n):
    start = pow(2, n - 1) + 1
    end = start * 2 - 1

    for num in xrange(start, end, 2):

        bnum = bin(num)[2:]
        no_primes = True

        factors = [None] * 9
        for base in xrange(2, 11):
            is_prime, factor = prime_or_factor(int(bnum, base=base))
            if is_prime:
                no_primes = False
                break
            factors[base - 2] = str(factor)

        if not no_primes:
             continue

        yield (bnum, factors)

test_cases = int(raw_input())

for test_case in xrange(test_cases):
    n, j = map(int, raw_input().split())

    print "Case #" + str(test_case + 1) + ":"

    current_j = 1
    for coin, factors in generate_possible_coins(n):
        print coin, ' '.join(factors)

        current_j += 1
        if current_j > j:
            break



