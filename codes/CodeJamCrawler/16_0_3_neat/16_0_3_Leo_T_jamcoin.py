import sys

from functools import reduce, lru_cache

from math import sqrt
from random import random

test_path = 'C-test.in'


def main(input_path=test_path):
    with open(input_path) as f:
        T = int(f.readline().strip())
        for t in range(T):
            # produce J different jamcoins of length N,
            N, J = (int(i) for i in f.readline().strip().split())
            coins, divs = solve(N, J)
            print("Case #{0}:".format(t + 1))
            for coin in coins:
                print("{0} {1}".format(coin, ' '.join(map(str, divs[coin].values()))))
            pass
            # print("Case #{0}: {1}".format(t + 1, solve(N, J)))


def solve(N, J):
    coins = set()
    divs = {}
    while len(coins) < J:
        # Make a new coin
        coin = ([str(int(random() > 0.5)) for _ in range(N)])
        coin[0] = '1'
        coin[-1] = '1'
        coin = ''.join(coin)
        if coin in coins:
            continue
        ans = is_valid(coin)

        if ans:
            coins.add(coin)
            divs[coin] = ans
            print(len(coins))

    return coins, divs


@lru_cache(maxsize=None)
def is_valid(coin):
    ans = {}
    for b in range(2, 11):
        num = int(coin, b)
        f = factors(num) - {1, num}
        if len(f) == 0:
            return False
        ans[b] = f.pop()
    return ans


@lru_cache(maxsize=None)
def factors(n):
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
