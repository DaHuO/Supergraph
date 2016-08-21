import itertools

file = "C-large.in"

class ShouldntGetHere(Exception): pass
class IsPrime(Exception): pass
class NotEnoughCoins(Exception): pass

def first_prime_factor(n, max_factor=11):
    if n < 2:
        raise ShouldntGetHere
        raise IsPrime

    if n % 2 == 0:
        if n == 2:
            raise ShouldntGetHere
            raise IsPrime
        return 2

    k = 3
    while k <= max_factor and k * k <= n:
        if n % k == 0:
            return k
        k += 2

    raise IsPrime

def jam_coin_prime_factors(i):
    return [first_prime_factor(int(i, base=base)) for base in range(2, 11)]

def coin_jam(N, J, fn=jam_coin_prime_factors):
    n = 0
    j = 0

    while j < J:
        try:
            coin = "1{}1".format("{0:b}".format(n).zfill(N - 2))
            if len(coin) > N:
                raise NotEnoughCoins

            yield itertools.chain([coin], fn(coin))

            j += 1
        except IsPrime:
            pass

        n += 1

with open(file) as handle:
  T = int(handle.readline())

  for t in range(T):
    N, J = map(int, handle.readline().split(' '))

    print "Case #{}:".format(t + 1)

    for line in coin_jam(N, J):
        print ' '.join(map(str, line))
