#!/usr/bin/env python

f = open('/dev/stdin', 'r')

T = int(f.readline())

def flip(cakes):
    for i in range(len(cakes)):
        if cakes[i] == '-':
            cakes[i] = '+'
        else:
            cakes[i] = '-'

    return cakes

for t in range(T):
    cakes = list(f.readline().strip())[::-1]

    flips = 0
    while '-' in cakes:
        i = cakes.index('-')
        cakes[i:] = flip(cakes[i:])
        flips += 1

    print('Case #%d: %d' % (t + 1, flips))
