#! /usr/bin/env python

from collections import Counter

uniques = {'Z': 0, 'W': 2, 'U': 4, 'X': 6, 'G': 8}
numbers = 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE'
numbers = {i: Counter(numbers[i]) for i in range(10)}
new_uniques = {'O': 1, 'T': 3, 'F': 5, 'S': 7}
new_new_uniques = {'N': 9}

T = int(raw_input())
for case in range(T):
    S = raw_input()
    digits = []
    c = Counter(S)
    u = uniques
    while any(c[unique] for unique in u):
        for unique in u:
            if c[unique]:
                c -= numbers[u[unique]]
                digits.append(u[unique])
    u = new_uniques
    while any(c[unique] for unique in u):
        for unique in u:
            if c[unique]:
                c -= numbers[u[unique]]
                digits.append(u[unique])
    u = new_new_uniques
    while any(c[unique] for unique in u):
        for unique in u:
            if c[unique]:
                c -= numbers[u[unique]]
                digits.append(u[unique])
    answer = ''.join(str(digit) for digit in sorted(digits))
    print 'Case #{}: {}'.format(case + 1, answer)
