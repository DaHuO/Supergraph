#!/usr/bin/python

f = 'a-sample.in'
f = 'A-small-attempt0.in'
f = 'A-large.in'


beats = {'P': 'R',
         'R': 'S',
         'S': 'P'}


def get_tree(top, depth):
    if depth == 0:
        return top
    a = get_tree(top, depth-1)
    b = get_tree(beats[top], depth-1)
    if a < b:
        return a + b
    else:
        return b + a


def solve(vals):
    n, r, p, s = tuple(map(int, vals))
    for top in 'RSP':
        tree = get_tree(top, n)
        if tree.count('R') == r and \
                tree.count('S') == s and \
                tree.count('P') == p:
            return tree
    return 'IMPOSSIBLE'


inp = map(str.strip, list(open(f))[1:])
t = 1
while inp:
    vals = tuple(inp.pop(0).split())
    print 'Case #%d: %s' % (t, solve(vals))
    t += 1
