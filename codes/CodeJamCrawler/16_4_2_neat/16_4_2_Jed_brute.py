#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $File: brute.py
# $Date: Sun May 29 00:01:44 2016 +0800
# $Author: jiakai <jia.kai66@gmail.com>

def cached(f):
    cache = {}
    def wf(*args):
        if args in cache:
            return cache[args]
        rst = f(*args)
        cache[args] = rst
        return rst
    return wf

def prob(plist):
    @cached
    def f(n, y):
        if n == y:
            ans = 1
            for i in plist[:n]:
                ans *= i
            return ans
        if n < y or n == 0:
            return 0
        p = plist[n - 1]
        return f(n - 1, y - 1) * p + f(n - 1, y) * (1 - p)

    l = len(plist)
    assert l % 2 == 0
    return f(l, l // 2)

def solve(plist, k):
    ans = 0

    N = len(plist)
    def dfs(pos, sub):
        nonlocal ans
        if pos == N:
            if len(sub) == k:
                ans = max(ans, prob(sub))
            return

        if N - (pos + 1) + len(sub) >= k:
            dfs(pos + 1, sub)

        sub.append(plist[pos])
        dfs(pos + 1, sub)
        sub.pop()

    dfs(0, [])
    return ans

def main():
    nr_case = int(input())
    for i in range(nr_case):
        n, k = map(int, input().split())
        plist = list(map(float, input().split()))
        assert len(plist) == n
        print('Case #{}: {}'.format(i + 1, solve(plist, k)))

if __name__ == '__main__':
    main()

