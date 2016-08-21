#!/usr/bin/python

import sys


if __name__ == '__main__':

    fname = sys.argv[-1]
    with open(fname, 'r') as f:
        lines = [l[:-1] for l in f.readlines()]

    outlines = []

    for i, line in enumerate(lines[1:]):
        n = 1
        s_pre = line[0]
        print line
        for s in line:
            if s != s_pre:
                n += 1
                s_pre = s
        if s == '+':
            n -= 1

        outlines.append('Case #%s: %s' % (i + 1, n))

    fname = fname[:-2] + 'out'
    with open(fname, 'w') as f:
        f.write('\n'.join(outlines))
