#!/usr/bin/env python

import fileinput

def resolve(k, c, s):
    if s < k:
        return 'IMPOSSIBLE'
    if k == 1:
        return '1'
    max = pow(k, c) - 1
    step = max / (k - 1)
    idx = [p * step for p in range(0, k)]
    return ' '.join(str(i+1) for i in idx)


if __name__ == "__main__":
    input = fileinput.input()
    nbtst = int(input.readline())
    for idx in range(nbtst):
        val = [int(v) for v in input.readline().split()]
        print 'Case #{}: {}'.format(idx+1, resolve(val[0], val[1], val[2]))
