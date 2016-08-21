from itertools import product, zip_longest
from math import ceil

import numpy as np

def perm_idx(perm, c):
    n = perm[0]
    for x in perm[1:]:
        n += x * c
        c *= c
    print('perm: ', perm, c,  n)
    return str(n+1)

# def solve(k, c, s):
def solve(x):
    k, c, s = x
    print(k, c, s)
    needed = ceil(k/c)
    if needed > s:
        return 'IMPOSSIBLE'
    if needed == k:
        return ' '.join(str(x+1) for x in range(k))
    chunks = np.array_split(np.arange(k), s)
    print(needed , list(chunks))
    res = []
    for chunk in chunks:
        print(chunk)
        res.append(perm_idx(chunk, k))
    print(k, c, s, res)
    return ' '.join(res)

def pre(s):
    return (int(x) for x in s.split())

if __name__ == '__main__':
    # solve((14, 12, 14))
    import gcj
    gcj.main(solve, pre)
    perm_idx([2], 3)

# # print(solve(2, 1, 2))
# print(solve(20, 7, 3))
# c = 3
# perm_idx((2, 2, 0), c)
