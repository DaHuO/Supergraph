#!/usr/bin/env python
from itertools import product, count, islice
from math import sqrt

def rebase(n, b):
    total = 0
    for i, digit in enumerate(reversed(list(str(n)))):
        total += (b**i)*int(digit)
    return total


def notPrime(n):
    for number in islice(count(2), int(sqrt(n) - 1)):
        if not n % number:
            return number
        # Looking at a million numbers is good enough...
        if number > 1000000:
            break
    return False


def list_coins(n, j):
    coin_list = []
    for inner_coin in product('01', repeat=n-2):
        coin = int('1'+''.join(inner_coin)+'1')
        div_list = []
        for coin_b10 in [rebase(coin, x) for x in range(2, 11)]:
            div = notPrime(coin_b10)
            if not div:
                break
            div_list.append(div)
        if len(div_list) == 9:
            coin_list.append((coin, div_list))
        if len(coin_list) == j:
            break
    return coin_list

# print list_coins(16, 50)
# print rebase(1001, 10)
# print notPrime(41)

t = int(raw_input())
for i in xrange(1, t + 1):
    print('Case #{}:'.format(i))
    in_n, in_j = (int(x) for x in raw_input().split())
    for coin, divs in list_coins(in_n, in_j):
        print('{} {}'.format(coin, ' '.join(str(x) for x in divs)))
