#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from itertools import permutations, product
from itertools import product
# import math

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True


def divisor_list(n_list):
    divs = []
    for x in n_list:
        for i in range(2, x):
            if x % i == 0:
                divs.append(i)
                break
    return divs

def bitGen(n):
    for i in product('01', repeat=n):
        yield ''.join(i)

cases = int(input().strip())

for i, x in enumerate(range(cases), 1):
    coinLength, numberOfCoins = list(map(int, input().strip().split()))
    tempLength = coinLength - 2
    choices = ('0' * tempLength) + ('1' * tempLength)
    # perms = permutations(choices, tempLength)
    perms = bitGen(tempLength)
    combos = ('1' + ''.join(y for y in t) + '1' for t in perms)

    jamcoins = []
    tried = []
    for seq in combos:
        if len(jamcoins) == numberOfCoins:
            break
        elif seq in tried:
            continue
        bases2_10 = [int(seq, base) for base in range(2, 11)]
        # import ipdb; ipdb.set_trace()
        if not any(is_prime(b) for b in bases2_10):
            jamcoins.append((seq, divisor_list(bases2_10)))
        tried.append(seq)

    print("Case #{0:s}:".format(str(i)))
    for coin in jamcoins:
        print(coin[0], ' '.join(str(x) for x in coin[1]))
