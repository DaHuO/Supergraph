#!/usr/bin/python

import sys
from itertools import product


def tr(x):
#    print x
    return x


def tonum(x):
    return int("".join(str(d) for d in x))


def fullscan(score):
    empty_idx = [i for i, d in enumerate(score) if d is None]
    for pr in product(range(10), repeat=len(empty_idx)):
        s = list(score)
        for i, d in zip(empty_idx, pr):
            s[i] = d
        assert all(d is not None for d in s)
        yield s


def solve(c, j):
    diff, c_score, j_score = min(
        tr((abs(tonum(c_score) - tonum(j_score)), c_score, j_score))
        for c_score in fullscan(c) for j_score in fullscan(j)
    )
    return c_score, j_score


def main():
    N = int(next(sys.stdin))
    for i in xrange(1, N+1):
        c, j = next(sys.stdin).strip().split()
        c = [None if ch == '?' else int(ch) for ch in c]
        j = [None if ch == '?' else int(ch) for ch in j]
        cc, jj = solve(c, j)
        print "Case #{}:".format(i), "".join(str(x) for x in cc), "".join(str(x) for x in jj)


if __name__ == '__main__':
    main()

