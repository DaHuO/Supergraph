#!/usr/bin/env python3

from collections import Counter

dgts = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

uniques = [
    (0, 'Z'),
    (2, 'W'),
    (6, 'X'),
    (7, 'S'),
    (5, 'V'),
    (4, 'F'),
    (8, 'G'),
    (3, 'H'),
    (1, 'O'),
    (9, 'E')
]


def solve(s):
    cnt = Counter(s)
    ds = []
    for d, c in uniques:
        n_found = cnt[c]
        ds += [d] * n_found
        for cc in dgts[d]:
            assert cnt[cc] >= n_found, (d, c, cnt)
            cnt[cc] -= n_found
    for v in cnt.values():
        assert v == 0
    ds.sort()
    return ''.join(str(d) for d in ds)


for i in range(int(input())):
    s = input()
    print("Case #%s: %s" % (i+1, solve(s)))