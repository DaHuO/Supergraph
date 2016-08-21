import sys
import math
sys.setrecursionlimit(10000)

T = int(raw_input())


def find_items(sss):
    itm = [""]

    for i, x in enumerate(sss):
        new_itm = []
        for s in itm:
            if x != '?':
                s += x
                new_itm.append(s)
            else:
                for xx in range(10):
                    ss = s + str(xx)
                    new_itm.append(ss)
        itm = new_itm

    return itm

for _test in range(1, T + 1):
    answer = ""

    C, J = raw_input().split()

    items_c = find_items(C)
    items_j = find_items(J)

    ans = (99**99, '','')

    for x in sorted(items_c):
        for y in sorted(items_j):
            n_x, n_y = int(x), int(y)

            if abs(n_x - n_y) < ans[0]:
                ans = (abs(n_x - n_y), x, y)

    print "Case #{}: {} {}".format(_test, ans[1], ans[2])

"""
Case #1: 19 20
Case #2: 023 023
Case #3: 0 0
Case #4: 05 00
"""