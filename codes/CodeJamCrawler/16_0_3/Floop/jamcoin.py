#!/usr/bin/env python3
import random
from miller_rabin import *

T = input()
N, J  = map(int, str.split(input()))

def generate_coin(j):
    coin = ['1']
    for i in range(j - 2):
        coin.append(str(int('0') + random.randint(0, 1)))
    coin.append('1')
    return ''.join(coin)

def check_coin(coin):
    divisors = []
    for b in range(2, 11):
        n = int(coin, base=b)

        if prime(n):
            return None
        
        d = 0
        for d in primes():
            if n % d == 0:
                break
            if d > 1000:
                return None

        divisors.append(d)

    return divisors


print('Case #1:')
coins = set()
while len(coins) < J:
    coin = generate_coin(N)
    if coin in coins:
        continue
    divisors = check_coin(coin)
    if divisors:
        print(' '.join([coin] + list(map(str, divisors))))
        coins.add(coin)
