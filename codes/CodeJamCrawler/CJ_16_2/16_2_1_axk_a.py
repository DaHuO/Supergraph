#!/usr/bin/env python3

import collections

def calc(s):
    ds = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    cc = collections.Counter()
    for c in s:
        cc[c] += 1
    r = []
    res = rec(ds, 0, cc, r)
    assert(res)
    return ''.join(r)

def is_empty(cc):
    for c in cc:
        if cc[c] > 0:
            return False
    return True

def rec(ds, i, cc, r):
    if i == len(ds):
        return is_empty(cc)

    exists = True
    for c in ds[i]:
        if cc[c] == 0:
            exists = False
            break
    if exists:
        for c in ds[i]:
            cc[c] -= 1
        r.append(str(i))

        if rec(ds, i, cc, r):
            return True

        for c in ds[i]:
            cc[c] += 1
        r.pop()

    return rec(ds, i+1, cc, r)

T = int(input())
for t in range(T):
    S = input()
    r = calc(S)
    print("Case #{}: {}".format(t + 1, r))

