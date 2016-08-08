#!/usr/bin/env python3

import sys
from collections import *

def print_sol(tc, ans):
    print('Case #{}: {}'.format(tc, ans))

def generate(cur, steps):
    for _ in range(steps):
        nxt = "".join([{"P": "PR", "R": "RS", "S": "PS"}[x] for x in cur])
        cur = nxt
    return cur, [cur.count(x) for x in "RPS"]

def sort_result(res):
    m = len(res) // 2
    a = res[0:m]
    b = res[m:]
    if len(a) > 1:
        a = sort_result(a)
        b = sort_result(b)
    assert a != b
    if a < b:
        return a + b
    return b + a

T = int(input())
for tc in range(1, T+1):
    N, R, P, S = [int(x) for x in input().split(' ')]

    done = False
    for start in "RPS":
        result, cnt = generate(start, N)
        if cnt == [R, P, S]:
            result = sort_result(result)
            print_sol(tc, result)
            done = True
            break

    if not done:
        print_sol(tc, "IMPOSSIBLE")
