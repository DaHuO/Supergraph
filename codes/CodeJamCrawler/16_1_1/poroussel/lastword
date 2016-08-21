#!/usr/bin/env python

import fileinput

def resolve(line):
    res = line[0]
    for l in line[1:]:
        if l >= res[0]:
            res = l + res
        else:
            res = res + l
    return res

if __name__ == "__main__":
    input = fileinput.input()
    nbtst = int(input.readline())
    for idx in range(nbtst):
        line = input.readline().strip()
        print 'Case #{}: {}'.format(idx+1, resolve(line))
