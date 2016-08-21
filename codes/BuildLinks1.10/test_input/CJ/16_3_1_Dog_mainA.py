#! /usr/bin/env python3

import sys

parties = tuple(chr(c) for c in range(ord('A'), ord('Z') + 1))

def insert_sorted(x, xs):
    if x[0] == 0: return
    i = 0
    while i < len(xs) and x[0] < xs[i][0]:
        i += 1
    xs.insert(i, x)

def trysolve(p, s, a, b):
    p1, p2, *ptail = p
    if p1[0] < a: return None
    if p2[0] < b: return None
    if (p1[0] - a) > (s - a - b)/2: return None
    if (p2[0] - b) > (s - a - b)/2: return None
    q1 = (p1[0] - a, p1[1])
    q2 = (p2[0] - b, p2[1])
    insert_sorted(q1, ptail)
    insert_sorted(q2, ptail)
    return (ptail, s - a - b)

def solve(problem):
    s = sum(t for (t, _) in problem)
    problem.sort(reverse=True)
    result = list()
    while s:
        if len(problem) == s:
            sol = trysolve(problem, s, 1, 0)
            ab = problem[0][1]
        else:
            sol = trysolve(problem, s, 2, 0)
            ab = problem[0][1]*2

        if sol is None:
            sol = trysolve(problem, s, 1, 1)
            ab = problem[0][1]+problem[1][1]
        if sol is None:
            sol = trysolve(problem, s, 1, 0)
            ab = problem[0][1]
        if sol is None:
            raise Exception('???')
        result.append(ab)
        problem, s = sol
        if s == 1: return 'Error'

    return ' '.join(result)

def parse(content):
    lines = content.split('\n')
    lines.reverse()
    T = int(lines.pop())
    for i in range(T):
        lines.pop()
        yield list(zip(map(int, lines.pop().split()), parties))


#################################################################

if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as f:
        content = f.read().strip()

    with open(filename + '.out', 'w') as out:   
        for (i, case) in enumerate(parse(content), 1):
            result = solve(case)
            for o in (out, sys.stdout):
                print('Case #', i, ': ', result, sep='', file=o)
