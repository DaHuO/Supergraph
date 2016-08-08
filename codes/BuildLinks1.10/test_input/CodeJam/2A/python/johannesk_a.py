import itertools
import functools

def combine(a, b):
    return min(a+b, b+a)

def mkposs(n):
    if n == 0:
        return [
            [0, 1],  # 0 wins
            [1, 2],  # 1 wins
            [0, 2],  # 2 wins
        ]
    a = mkposs(n-1)
    return [
        combine(a[0], a[1]),
        combine(a[1], a[2]),
        combine(a[2], a[0])
    ]

def cumul(xs):
    c = [0]*3
    for x in xs:
        c[x] += 1
    return tuple(c)

ans = {}

for i in range(13):
    for x in mkposs(i):
        ans[cumul(x)] = ''.join(map(lambda i: "PRS"[i], x))

def solve(n, r, p, s):
    return ans.get((p, r, s), "IMPOSSIBLE")

def parse():
    return map(int, input().split())

for t in range(int(input())):
    print("Case #{}: {}".format(t+1, solve(*parse())))
