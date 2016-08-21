#! /usr/bin/env python3

from itertools import combinations
from decimal import Decimal
import sys

for _ in range(int(input())):
    n, k = (int(i) for i in input().split())
    p = sorted(Decimal(i) for i in input().split())

    ans = Decimal('0')
    for i in range(k + 1):
        r = list(range(n))
        pp = r[:i] + r[n - k + i:]
        cur = 0
        for c in combinations(pp, k // 2):
            x = 1
            for i in pp:
                if i in c:
                    x *= p[i]
                else:
                    x *= 1 - p[i]
            cur += x
        ans = max(ans, cur)

    print('Case #{}: {}'.format(_ + 1, ans))
    print('Case #{}'.format(_ + 1), file=sys.stderr)
