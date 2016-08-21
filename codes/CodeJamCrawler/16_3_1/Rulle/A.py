import sys
from itertools import permutations
sys.setrecursionlimit(200000)

def _solve(P):
    tot = sum(P)
    m = max(P)
    if m > tot / 2 or _solve.solved:
        yield None
        return

    if tot == 0:
        _solve.solved = True
        yield ""
        return

    for i, p in enumerate(P):
        if p == 0:
            continue
        for j, p2 in enumerate(P[i:]):
            if i == j and p < 2:
                continue
            if p2 == 0:
                continue
            Q = list(P)
            Q[i] -= 1
            Q[j] -= 1
            for alt in _solve(Q):
                if alt is not None:
                    yield chr(ord('A')+i) + chr(ord('A')+j) + " " + alt

    for i, p in enumerate(P):
        if p == 0:
            continue
        if p < m:  # KANSKE
            continue
        Q = list(P)
        Q[i] -= 1
        for alt in _solve(Q):
            if alt is not None:
                yield chr(ord('A')+i) + " " + alt

def solve(P):
    _solve.solved = False
    ans = list(_solve(P))
    # print ans
    assert _solve.solved
    assert len(ans) == 1
    return ans[0].strip()
    

if __name__ == "__main__":
    f = open("A.in")

    lines = f.read().splitlines()
    interp_line = lambda x: map(int, x.split(" "))
    T = int(lines.pop(0))
    for t in range(T):
        N = int(lines.pop(0))
        P = map(int, lines.pop(0).strip().split(" "))
        assert len(P) == N
        ans = solve(P)

        print "Case #%d: %s" % (1+t, ans)
    """
    for idx, line in enumerate(lines[1:]):
        print "Case #%d: %s" % (1+idx, solve(M, line))
    """
    f.close()
