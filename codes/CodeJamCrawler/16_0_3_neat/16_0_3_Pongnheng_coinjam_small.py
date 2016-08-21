#!/usr/bin/python

import itertools
import math

def generate_numbers():
    numbers = []
    for i in itertools.product([0, 1], repeat=14):
        n = (1,) + i + (1,)
        binary_string = ''.join(map(str, n))
        numbers.append(binary_string)
    return numbers

def is_prime(n):
    if n == 1: return False # 1 is not prime
    elif n < 4: return True # 2, 3 is prime
    elif n % 2 == 0: return False # even is not prime
    elif n < 9: return True # excluded 4,6,8 already, so the rest is prime
    elif n % 3 == 0: return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0: return False
            if n % (f + 2) == 0: return False
            f = f + 6
    return True

def has_prime(numbers):
  for n in numbers:
      if is_prime(n): return True
  return False

def find_non_trivial_divisor(n):
    r = math.floor(math.sqrt(n))
    f = 2
    while f <= r:
        if n % f == 0: return f
        f = f + 1
    return 0


def show_coin(coins):
    print "Case #1:"
    for c in coins:
        print c[0], c[1]

J = generate_numbers()
jamcoins = []

for n in J:
    all_base = [int(n, i) for i in range(2, 11)]
    if not has_prime(all_base):
        Ks = [find_non_trivial_divisor(b) for b in all_base]

        if 0 not in Ks and len(jamcoins) < 50:
            jamcoins.append((n, ' '.join(map(str, Ks))))
        else:
            break

show_coin(jamcoins)


         








    