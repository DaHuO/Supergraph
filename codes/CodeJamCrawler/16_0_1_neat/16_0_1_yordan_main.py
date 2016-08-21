#!/usr/bin/env python

import sys


def digits(x):
    x = abs(x)
    d = []
    while x:
        d.append(x % 10)
        x //= 10
    return d or [0]


def gen(x):
    i = 1
    while 1:
        yield x * i
        i += 1


def read_input(f):
    N = int(f.readline())
    inputs = []
    for line in f:
        inputs.append(int(line))
    assert len(inputs) == N
    return inputs


def solve(x):
    if x == 0:
        return 'INSOMNIA'
    mask = 0x0
    for y in gen(x):
        for d in digits(y):
            assert d <= 10
            mask |= (1 << d)
            if mask == 0b1111111111:
                return y
    return 'Damn...'


def main():
    inputs = read_input(sys.stdin)
    for i, x in enumerate(inputs, start=1):
        # print('i={}, x={}'.format(i, digits(x)))
        print('Case #{}: {}'.format(i, solve(x)))


if __name__ == '__main__':
    main()
    
