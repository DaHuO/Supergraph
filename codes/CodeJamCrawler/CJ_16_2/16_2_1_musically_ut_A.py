#!/usr/bin/env python
from collections import defaultdict

T = int(input())
ii = 1

nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def count(dgs, char, nstr):
    c = 0
    while dgs[char] > 0:
        c += 1
        for x in nstr: dgs[x] -= 1

    return c


# ZERO Z
# TWO W
# FOUR U
# SIX X
# EIGHT G
#
# ONE O
# THREE T
# FIVE F
# SEVEN S
#
# NINE
#

def get_ph_digits(dgs):
    d = {}
    d[0] = count(dgs, 'Z', 'ZERO')
    d[2] = count(dgs, 'W', 'TWO')
    d[4] = count(dgs, 'U', 'FOUR')
    d[6] = count(dgs, 'X', 'SIX')
    d[8] = count(dgs, 'G', 'EIGHT')

    d[1] = count(dgs, 'O', 'ONE')
    d[3] = count(dgs, 'T', 'THREE')
    d[5] = count(dgs, 'F', 'FIVE')
    d[7] = count(dgs, 'S', 'SEVEN')

    d[9] = count(dgs, 'N', 'NINE')

    assert all(dgs[x] == 0 for x in dgs)

    return ''.join(str(x) * d[x] for x in range(0, 10))

while ii <= T:
    r = input()
    dgs = defaultdict(lambda : 0)
    for x in r:
        dgs[x] += 1

    print('Case #{}: {}'.format(ii, get_ph_digits(dgs)))
    ii += 1


###

# for n in ["ONE", "THREE", "FIVE", "SEVEN", "NINE"]:
#     for d in n:
#         for m in ["ONE", "THREE", "FIVE", "SEVEN", "NINE"]:
#             if m == n:
#                 continue
#
#             if d in m:
#                 break
#         else:
#             print(n, d)




