#!/usr/bin/python3
# -*- coding: utf-8 -*-


def calc(win, n):
    if n == 0:
        return win
    p = calc(win, n-1)
    if win == 'P':
        p2 = calc('R', n-1)
    elif win == 'R':
        p2 = calc('S', n-1)
    else:
        p2 = calc('P', n-1)
    if p < p2:
        return p + p2
    return p2 + p


def solve():
    n, r, p, s = map(int, input().split())
    res = sorted([calc('P', n), calc('R', n), calc('S', n)])
    for line in res:
        if line.count('P') == p and line.count('R') == r:
            return line
    return 'IMPOSSIBLE'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print('Case #%d:' % (i+1), solve())
