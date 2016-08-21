#!/usr/local/bin/python3
import numpy as np
c = int(input())

ns = np.array([input().strip() for case in range(c)])


table = [(idx, list(item))
         for item, idx in [("ZERO", 0), ("EIGHT", 8), ("SIX", 6), ("TWO", 2), ("FOUR", 4)]]
table2 = [(idx, list(item)) for item, idx in [("ONE", 1), ("THREE", 3),
                                              ("FIVE", 5), ("SEVEN", 7), ("NINE", 9)]]

# NORUIFNE


def solve(s):
    ll = list(s)
    rr = []

    while len(ll) > 0:
        check_continue = False
        for idx, ccs in table:
            set1 = set(ccs)
            if sum([ccs.count(ch) <= ll.count(ch) for ch in set1]) == len(set1):
                for ch in ccs:
                    ll.remove(ch)
                rr.append(str(idx))
                if len(ll) == 0:
                    break
                check_continue = True
        if not check_continue:
            break

    while len(ll) > 0:
        check_continue = False
        for idx, ccs in table2:
            set1 = set(ccs)
            if sum([ccs.count(ch) <= ll.count(ch) for ch in set1]) == len(set1):
                for ch in ccs:
                    ll.remove(ch)
                rr.append(str(idx))
                if len(ll) == 0:
                    break
                check_continue = True
        if not check_continue:
            break

    rr.sort()
    return "".join(rr)

vfunc = np.vectorize(solve)

for case, item in enumerate(vfunc(ns)):
    print ('Case #{}: {}'.format(case + 1, item))
