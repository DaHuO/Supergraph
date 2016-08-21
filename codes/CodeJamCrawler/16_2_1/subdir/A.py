#!/usr/bin/python

import sys
from collections import Counter


DIGS = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")


def pop(st, d):
    if all(st[l] > 0 for l in DIGS[d]):
        for l in DIGS[d]:
            st[l] -= 1
        return True
    else:
        return False


def push(st, d):
    for l in DIGS[d]:
        st[l] += 1


def solve(st, smallest=0):
    if all(c==0 for c in st.itervalues()):
        return []
    else:
        not_found = True
        for d in range(smallest, 10):
            if pop(st, d):
                not_found = False
                tail = solve(st, d)
                push(st, d)
                if tail is not None:
                    return [d] + tail
        if not_found:
            return None


def main():
    N = int(next(sys.stdin))
    for i in xrange(1, N+1):
        s = next(sys.stdin).strip()
        print "Case #{}:".format(i), "".join(str(d) for d in solve(Counter(s)))


if __name__ == '__main__':
    main()

