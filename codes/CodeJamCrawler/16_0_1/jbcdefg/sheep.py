#!/usr/bin/python

import sys


if __name__ == '__main__':

    fname = sys.argv[-1]
    with open(fname, 'r') as f:
        lines = [l[:-1] for l in f.readlines()]

    outlines = []

    for i, line in enumerate(lines[1:]):
        N = int(line)
        if N == 0:
            o = 'INSOMNIA'
        else:
            digits = [False for _ in xrange(10)]
            k = 1
            while True:
                for d in str(k * N):
                    digits[int(d)] = True
                if all(digits):
                    break
                k += 1
            o = k * N

        outlines.append('Case #%s: %s' % (i + 1, o))

    fname = fname[:-2] + 'out'
    with open(fname, 'w') as f:
        f.write('\n'.join(outlines))
