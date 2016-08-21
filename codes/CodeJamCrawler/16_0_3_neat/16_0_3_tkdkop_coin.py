#!/usr/bin/env python
import sys
import math
from primes import primes


m = sys.stdin.readline()
i = 0
length, n = sys.stdin.readline().strip().split(' ')
print 'Case #1:'


def prime_divisor(n):
    stop_at = math.sqrt(n)
    i = 0
    for i in primes:
        if i > stop_at:
            return None
        if n % i == 0:
            return i
    return None

#     while i <= stop_at:
#         i = get_next_prime()
#         if n % i == 0:
#             return i
#
# def get_next_prime():
#     global prime_numbers
#     next_candidate = prime_numbers[-1]
#     while True:
#         next_candidate += 2
#         stop_at = math.sqrt(next_candidate)
#         for i in prime_numbers:
#             if i > stop_at:
#                 prime_numbers.append(next_candidate)
#                 return prime_numbers[-1]
#             if next_candidate % i == 0:
#                 continue

def generate_jamcoins(length, qq):
    i = -1
    found = 0
    while True:
        i += 1

        st = '{0:b}'.format(i)
        st =  st.rjust(length, '0')
        if len(st) > length:
            print 'FAILED'
            break
        st = '1%s1' % st
        numbers = [int(st, j) for j in range(2,11)]
        divisor_list = []
        for n in numbers:
            d = prime_divisor(n)
            if d is None:
                break
            divisor_list.append(d)
        if len(numbers) == len(divisor_list):
            found += 1
            out = st
            for j,k in zip(numbers, divisor_list):
                out += ' %d' % (k)
            print out

        if found == qq:
            break



generate_jamcoins(int(length)-2, int(n))

