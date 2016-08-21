#!/usr/bin/env python3
import math

J = 50
N = 16

def bin_gen(n):
    if n == 1:
        yield [0]
        yield [1]
    else:
        for i in bin_gen(n-1):
            yield [0] + i
            yield [1] + i

def as_base(num, base):
    return sum([base**i*num[i] for i in range(len(num))])

def jam_gen(n):
    for i in bin_gen(n-2):
        j = [1] + i + [1]
        yield j

def get_factor(num):
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            return i
    return None

print("Case #1:")
num_sols = 0
for num in jam_gen(N):
    if num_sols == J:
        break
    is_jam = True
    factors = []
    for j in range(2, 11):
        factor = get_factor(as_base(num, j))
        if factor is None:
            is_jam = False
            continue
        else:
            factors.append(factor)
    if is_jam:
        num_sols += 1
        num.reverse()
        print(''.join([str(i) for i in num]), *factors)
