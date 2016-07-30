import sys

def _cc():
    for line in sys.stdin:
        for x in line.strip().split():
            yield x

_cin = _cc()
cin = _cin.next

OTHER = {
        'R': 'S',
        'S': 'P',
        'P': 'R'
        }

memo = {}
def make_tree(ch, levels):
    if levels == 0:
        return ch
    ky = (ch, levels)
    if ky in memo:
        return memo[ky]
    tree1 = make_tree(ch, levels-1)
    tree2 = make_tree(OTHER[ch], levels-1)
    if tree1 < tree2:
        ret = tree1 + tree2
    else:
        ret = tree2 + tree1
    memo[ky] = ret
    return ret

def solve(N, R, P, S):
    out = None
    for ch in 'RPS':
        mytree = make_tree(ch, N)
        cts = {'R': 0, 'P': 0, 'S': 0}
        for cc in mytree:
            cts[cc] += 1
        if cts['R'] == R and cts['P'] == P and cts['S'] == S:
            if out is None:
                out = mytree
            else:
                out = min(out, mytree)
    if out is None:
        out = "IMPOSSIBLE"
    return out


T = int(cin())
for cn in xrange(1,T+1):
    N, R, P, S = [int(cin()) for t in xrange(4)]
    print "Case #%d: %s" % (cn, solve(N, R, P, S))


