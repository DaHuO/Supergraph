T = input()
from itertools import *
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

from collections import Counter

def ok(s, k):
    x = Counter([(a, b) for a, b, c in s])
    y = Counter((a, c) for a, b, c in s)
    z = Counter((b, c) for a, b, c in s)
    return max(x.values()) <= k and max(y.values()) <= k and max(z.values()) <= k


def solve(a, b, c, k):
    # print a, b, c, k
    if k >= 3:
        return a * b * c, [(x, y, z) for x, y, z in product(range(a), range(b), range(c))]

    if (a, b, c) == (3, 3, 3):
        if k == 2:
            return 18, [(0, 0, 0), (0, 0, 2), (0, 1, 1), (0, 1, 2), (0, 2, 0), (0, 2, 1), (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 2, 0), (1, 2, 2), (2, 0, 0), (2, 0, 1), (2, 1, 0), (2, 1, 2), (2, 2, 1), (2, 2, 2), (1, 1, 1)]
        if k == 1:
            return 9, [(0, 0, 2), (0, 1, 1), (0, 2, 0), (1, 0, 1), (1, 1, 0), (1, 2, 2), (2, 0, 0), (2, 1, 2), (2, 2, 1)]

    if (a, b, c) == (2, 3, 3):
        if k == 2:
            return 12, ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 2), (0, 2, 1), (0, 2, 2), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 2), (1, 2, 1), (1, 2, 2))
        if k == 1:
            return 6, ((0, 0, 0), (0, 1, 1), (0, 2, 2), (1, 0, 1), (1, 1, 2), (1, 2, 0))

    ct, bs = 0, []
    for s in powerset(product(range(a), range(b), range(c))):
        if not s: continue
        if ok(s, k) and len(s) > ct:
            ct, bs = len(s), s
    return ct, bs

for i in range(1, T + 1):
    j, p, s, k = map(int, raw_input().strip().split())
    v, a = solve(j, p, s, k)
    # print v, a
    assert v == len(a)
    assert ok(a, k)
    print 'Case #{}: {}'.format(i, str(v) + '\n' + '\n'.join('{} {} {}'.format(q + 1, r + 1, s + 1) for q, r, s in a))

#
# import random
# l = list(product(range(3), range(3), range(3)))
# m, s = 0, []
# while True:
#     rs = [random.randint(0, 1) for i in range(27)]
#     subs = [l[i] for i in range(27) if rs[i]]
#     if len(subs) < 16: continue
#     if ok(subs, 2) and len(subs) >= 17:
#         for x in l:
#             if x not in subs and ok(subs +[x], 2):
#                 print 'GOOD', subs + [x]
#     if ok(subs, 2) and len(subs) > m:
#         m, s = len(subs), sorted(subs)
#         print m, s

# q = [(0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 2, 1), (0, 2, 2), (1, 0, 0), (1, 0, 2), (1, 1, 1), (1, 1, 2), (1, 2, 0), (1, 2, 1), (2, 0, 0), (2, 0, 1), (2, 1, 1), (2, 1, 2), (2, 2, 0), (2, 2, 2)]
# for x in l:
#     if x not in q and ok(q +[x], 2):
#         print q, x
