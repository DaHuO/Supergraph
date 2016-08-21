#!/usr/bin/python3

import scipy as sp  # noqa
import math  # noqa


def next_line_to_ints(lines):
    return map(int, next(lines).split(' '))

# Don't check stuff that is not divisable by something smaller than 8000
max_checked = 8000


def first_divisor(n):
    """
    Returns None if prime otherwise first divisor
    """
    max_divisor = math.sqrt(n)

    # Not needed since it is uneven
    # if n == 2:
    #     return None
    # if n % 2 == 0:
    #     return 2

    d = 3
    while d <= max_divisor and d < max_checked:
        if n % d == 0:
            return d
        d += 2
    return None

f_in = open('c.in')
f_out = open('c.out', 'w')

lines = (i for i in f_in.read().splitlines())
t = int(next(lines))

n, j = tuple(next_line_to_ints(lines))

f_out.write('Case #1:\n')

for i in range(2**(n-2)):
    s = "1{}1".format(format(i, '030b'))

    divisors = []

    for base in range(2, 11):
        div = first_divisor(int(s, base))

        if div is None:
            break

        divisors.append(div)

    else:
        j -= 1
        output = '{} {}\n'.format(s, ' '.join(map(str, divisors)))
        f_out.write(output)
        print(j, output)

    if j == 0:
        break
