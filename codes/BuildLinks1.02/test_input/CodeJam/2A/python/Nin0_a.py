#!/usr/bin/python3

import sys


looser = {
    'R': 'S',
    'S': 'P',
    'P': 'R',
}

def find_sol(winner, n):
    if n == 0:
        return winner
    a = find_sol(winner, n - 1)
    b = find_sol(looser[winner], n - 1)
    if a > b:
        a, b = b, a
    return a + b

def count(niz):
    r, p, s = 0, 0, 0
    for x in niz:
        if x == 'R':
            r += 1
        elif x == 'P':
            p += 1
        else:
            s += 1
    return (r, p, s)

sol = dict()


for i in range(1, 12 + 1):
    r = find_sol('R', i)
    s = find_sol('S', i)
    p = find_sol('P', i)
    sol[i] = {count(r): r, count(p): p, count(s): s}

t = int(sys.stdin.readline())
for testCase in range(1, t + 1):
    n, r, p, s = [int(x) for x in sys.stdin.readline().split()]
    if (r, p, s) in sol[n]:
        print('Case #{0}: {1}'.format(testCase, sol[n][(r, p, s)]))
    else:
        print('Case #{0}: IMPOSSIBLE'.format(testCase))