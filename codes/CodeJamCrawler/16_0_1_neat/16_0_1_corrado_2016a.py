# -*- coding: utf-8 -*-

from pprint import pprint as _p


def get_digits(val):
    digits = set()
    while val:
        digits.add(val % 10)
        val //= 10
    return digits

with open('2016_a.in') as f:
    with open('2016_a.out', 'w') as fo:
        lines = f.readlines()
        t = int(lines[0].strip())
        for i in range(1, t + 1):
            number = int(lines[i].strip())

            seen = set()
            j = 0
            while len(seen) < 10:
                j += 1
                seen.update(get_digits(number * j))
                if j > 3 and len(seen) <= 1:
                    break
            if len(seen) != 10:
                fo.write('Case #{}: INSOMNIA\n'.format(i))
            else:
                fo.write('Case #{}: {}\n'.format(i, number * j))
