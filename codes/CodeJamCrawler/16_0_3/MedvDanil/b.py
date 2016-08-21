import numpy as np
from sys import argv

prim_lim = 10000

def to_rad(v, r):
    res = 0
    m = 1
    while v > 0:
        res += m * (v & 1)
        m *= r
        v >>= 1
    return res

def get_div(n):
    lim = min(int(n ** 0.5 + 1), prim_lim)
    pdiv = np.array(range(2, lim + 1))
    div = np.where((n % pdiv) == 0)[0]
    if len(div) == 0:
        return 0
    return div[0] + 2


def check(n):
    res = []
    for radix in range(2, 11):
        p = get_div(to_rad(n, radix))
        if p:
            res.append(p)
        else:
            return 0
    print(' '.join(map(str, [to_rad(n, 10)] + res)))
    return 1


n, j = map(int, argv[1:3])
print("Case #1:")
n = (1 << (n - 1)) + 1
while j > 0:
    j -= check(n)
    n += 2
