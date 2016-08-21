#!/usr/bin/env python3

from functools import lru_cache

TEST = 'large'
IN = 'B-{}.in'.format(TEST)
OUT = 'B-{}.out'.format(TEST)


def run(n, k, p):
    p.sort()

    @lru_cache(maxsize=None)
    def fn(m, y):
        if y > m or y < 0:
            return 0.0
        if m == 0:
            return 1.0
        return fn(m-1, y) * (1 - committee[m-1]) + fn(m-1, y-1) * committee[m-1]

    best, bcomm = -1, []
    for i in range(k + 1):
        committee = p[:k-i] + p[n-i:]
        fn.cache_clear()
        res = fn(k, k // 2)
        if res > best:
            best, bcomm = res, committee
    return best


def main():
    with open(IN) as fin, open(OUT, 'w') as fout:
        t = int(fin.readline().strip())
        for i in range(t):
            n, k = map(int, fin.readline().split())
            p = list(map(float, fin.readline().split()))
            assert len(p) == n
            res = run(n, k, p)
            print('Case #{}: {:.6f}'.format(i + 1, res), file=fout)
            print('Case #{}: {:.6f}'.format(i + 1, res))


if __name__ == '__main__':
    main()
