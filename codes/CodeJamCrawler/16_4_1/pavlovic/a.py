"""Google Code Jam 2016 - Round 2 - Problem A."""

import sys


def solve(winner, rounds):
    """Solver."""
    if rounds == 0:
        return winner
    if winner == 'R':
        finalist = 'S'
    elif winner == 'P':
        finalist = 'R'
    else:
        finalist = 'P'

    half1 = solve(winner, rounds - 1)
    half2 = solve(finalist, rounds - 1)

    if (half1 + half2 < half2 + half1):
        return half1 + half2
    return half2 + half1


def cnt(competitors):
    """Counter."""
    res = {'R': 0, 'P': 0, 'S': 0}
    for i in range(len(competitors)):
        res[competitors[i]] += 1

    return res

t = int(sys.stdin.readline().strip())

for i in range(t):
    n, r, p, s = map(int, sys.stdin.readline().strip().split())

    sol = None
    for win in ['R', 'P', 'S']:
        competitors = solve(win, n)
        c = cnt(competitors)
        if (c['R'] == r) and (c['P'] == p) and (c['S'] == s):
            if (sol is None) or (sol > competitors):
                sol = competitors

    print "Case #%d: %s" % (i + 1, 'IMPOSSIBLE' if sol is None else sol)
