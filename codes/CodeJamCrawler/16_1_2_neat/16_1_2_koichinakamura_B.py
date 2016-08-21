from numpy import *
def solve(lines):
    lines = array(lines)
    vs, cs = unique(lines, return_counts=True)
    return sorted(vs[cs%2==1])

for c in range(input()):
    N = input()
    lines = [
            map(int, raw_input().split())
            for i in range(2*N-1)
            ]
    ans = solve(lines)
    assert len(ans) == N
    print 'Case #{}: {}'.format(c+1, ' '.join(map(str, ans)))
