#!/usr/bin/python

import sys

def tobase(K, n):
    ''' return number n in base K '''
    out = 0
    for x, b in enumerate(n[::-1]):
        out += K ** x * min(b, K-1)
    return out

def get_pts(K, C):
    if C == 0:
        test = range(K)
    else:
        test = [tobase(K, v) for v in [
                    [2 * i + r for r in xrange(C+1)] \
                        for i in xrange(max((K - C) / 2 + 1, 1))]]
        assert(test[-1] < K ** (C + 1)) #safety check
    return test


if __name__ == '__main__':

    fname = sys.argv[-1]
    with open(fname, 'r') as f:
        lines = f.readlines()

    testcases = int(lines.pop(0))
    outlines = []
    for i, line in enumerate(lines):
        K, C, S = [int(v) for v in line.split(' ')]
        pts = [str(v + 1) for v in get_pts(K, C - 1)]
        if len(pts) > S:
            pts = ['IMPOSSIBLE']
        outlines.append('Case #%s: %s' % (i + 1, ' '.join(pts)))
    fname = fname[:-2] + 'out'
    print fname
    with open(fname, 'w') as f:
        f.write('\n'.join(outlines))

