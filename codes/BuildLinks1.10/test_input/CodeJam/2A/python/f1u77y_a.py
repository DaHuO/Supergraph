#! /usr/bin/env python3

import sys

def first_lineup(n, r, p, s):
    #print('first_lineup({n}, {r}, {p}, {s})'.format(**locals()), file=sys.stderr)
    if n == 1:
        if max(r, p, s) > 1:
            raise ValueError
        return 'P' * p + 'R' * r + 'S' * s
    m = min(r, p, s)
    dp, dr, ds = p - m, r - m, s - m
    if n % 2 == 1:
        m3 = m // 2
        if dp == dr == 1 and ds == 0:
            lp, lr, ls = 1, 0, 0
            rp, rr, rs = 0, 1, 0
        elif dr == ds == 1 and dp == 0:
            lp, lr, ls = 0, 1, 0
            rp, rr, rs = 0, 0, 1
        elif dp == ds == 1 and dr == 0:
            lp, lr, ls = 1, 0, 0
            rp, rr, rs = 0, 0, 1
        else:
            raise ValueError
        left = first_lineup(n - 1, m3 + lr, m3 + lp, m3 + ls)
        right = first_lineup(n - 1, m3 + rr, m3 + rp, m3 + rs)
        return left + right
    else:
        m3 = (m + 1) // 2
        if dp == dr == 0 and ds == 1:
            lp, lr, ls = 0, 1, 0
            rp, rr, rs = 1, 0, 0
        elif dr == ds == 0 and dp == 1:
            lp, lr, ls = 0, 0, 1
            rp, rr, rs = 0, 1, 0
        elif dp == ds == 0 and dr == 1:
            lp, lr, ls = 0, 0, 1
            rp, rr, rs = 1, 0, 0
        else:
            raise ValueError
        left = first_lineup(n - 1, m3 - lr, m3 - lp, m3 - ls)
        right = first_lineup(n - 1, m3 - rr, m3 - rp, m3 - rs)
        return left + right


t = int(input())
for _ in range(t):
    n, r, p, s = (int(i) for i in input().split())

    try:
        ans = first_lineup(n, r, p, s)
    except ValueError:
        ans = 'IMPOSSIBLE'

    print('Case #{}: {}'.format(_ + 1, ans))
