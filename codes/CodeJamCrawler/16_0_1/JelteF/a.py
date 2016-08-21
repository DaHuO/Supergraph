#!/usr/bin/python3

from itertools import count


def next_line_to_ints(lines):
    return map(int, next(lines).split(' '))

f_in = open('a.in')
f_out = open('a.out', 'w')

lines = (i for i in f_in.read().splitlines())
t = int(next(lines))

for case in range(1, t+1):
    n = int(next(lines))
    seen = set()

    if n > 0:
        for num in count(n, n):
            seen = seen.union(str(num))
            if len(seen) == 10:
                break
    else:
        num = 'INSOMNIA'

    f_out.write('Case #{}: {}\n'.format(case, num))
