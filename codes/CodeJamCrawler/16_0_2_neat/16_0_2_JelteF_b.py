#!/usr/bin/python3

from itertools import count  # noqa


def next_line_to_flts(lines):
    return map(float, next(lines).split(' '))

f_in = open('b.in')
f_out = open('b.out', 'w')

lines = (i for i in f_in.read().splitlines())
t = int(next(lines))

for case in range(1, t+1):
    s = next(lines)

    for i in count(0):
        s = s.rstrip('+')
        if len(s) == 0:
            break

        if s.startswith('-'):
            s = s[::-1]
            s = ''.join(['+' if c == '-' else '-' for c in s])
        else:
            minus = s.find('-')
            s = '-' * minus + s[minus:]

    f_out.write('Case #{}: {}\n'.format(case, i))
