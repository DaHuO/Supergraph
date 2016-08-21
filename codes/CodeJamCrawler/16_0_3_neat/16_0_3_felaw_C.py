#!/usr/bin/env python3
from random import choice

from math import sqrt


def random_coin(size):
    middle = ''.join(choice('01') for _ in range(size-2))
    return '1%s1' % middle


def convert(string, base):
    num = 0
    for digit in string:
        num *= base
        num += int(digit)
    return num


def non_prime(num):
    upper = min(int(sqrt(num))+1, 1000)
    for divisor in range(2, upper):
        if num % divisor == 0:
            return divisor
    return False


def is_valid(coin):
    res = []
    for base in range(2, 11):
        div = non_prime(convert(coin, base))
        if div:
            res.append(div)
        else:
            # was prime
            return None
    return res


size, n_coins = 32, 500
print("Case #1:")
remaining = n_coins
seen = set()
while remaining > 0:
    coin = random_coin(size)
    if coin in seen:
        continue
    divs = is_valid(coin)
    if divs:
        print(str(coin) + ' ' + ' '.join(str(n) for n in divs))
        remaining -= 1
        seen.add(coin)
