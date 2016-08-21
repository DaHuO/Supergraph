#!/usr/bin/env python

import fileinput

def resolve(pancakes):
    while pancakes[-1] == '+':
        pancakes.pop()
        if not len(pancakes):
            return 0
    num = 1
    last = pancakes[0]
    for p in pancakes[1:]:
        if p != last:
            num += 1
            last = p
    return num


if __name__ == "__main__":
    input = fileinput.input()
    nbtst = int(input.readline())
    for idx in range(nbtst):
        pancakes = list(input.readline().strip('\n'))
        print 'Case #{}: {}'.format(idx+1, resolve(pancakes))
