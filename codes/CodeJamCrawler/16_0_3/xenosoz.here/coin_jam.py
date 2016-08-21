#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Google Code Jam: Qualification Round 2016
# Problem C. Coin Jam
#
# by xenosoz on Apr 10, 2016.
#

# SymPy: A Python library for symbolic mathematics.
# http://www.sympy.org/en/index.html
from sympy.ntheory import factorint
import random

base_range = range(2, 10+1)

def random_coin(N):
    return "1" + "".join(random.choice("01") for x in range(N-2)) + "1"

def format_coin(coin):
    global base_range
    ret = coin
    for base in base_range:
        factors = factorint(int(coin, base), limit=1000)
        if len(factors) == 1:
            raise ValueError("Coin %s cannot be factored easily in base %d" % (coin, base))
        ret += " " + str(min(factors))
    return ret


def farm_coins(N, J):
    coins = set()
    while len(coins) < J:
        try:
            coin = random_coin(N)
            if coin in coins:
                continue
            print(format_coin(coin))
            coins.add(coin)
        except ValueError as e:
            continue
    return coins


if __name__ == '__main__':    
    T = int(input())
    for t in range(1, T+1):
        N, J = map(int, input().split())
        print("Case #%d:" % t)
        farm_coins(N, J)
