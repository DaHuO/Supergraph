#!/usr/bin/env python

import sys


def get_digits(n):
    digits = []
    while n != 0:
        digits.append(n % 10)
        n = n / 10
    return list(set(digits))

input_file = sys.argv[1]

with open(input_file) as f:
    n_tests = int(f.readline().strip())
    ns = []
    for i in range(n_tests):
        ns.append(int(f.readline().strip()))

results = []
for n in ns:
    if n == 0:
        results.append('INSOMNIA')
    else:
        seen_digits = []
        i = 1
        while len(seen_digits) != 10:
            seen_digits = list(set(seen_digits + get_digits(n * i)))
            i += 1
        results.append(n * (i - 1))

for i, result in enumerate(results):
    print 'Case #{}: {}'.format(i+1, result)
