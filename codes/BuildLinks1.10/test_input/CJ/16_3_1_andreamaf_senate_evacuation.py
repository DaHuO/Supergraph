
def check(P):
    s = sum(P)
    for p in P:
        if p*2 > s:
            return False
    return True


def solve(t):
    N = input()
    P = map(int, raw_input().split())

    ans = []
    while sum(P):
        if not check(P):
            raise Exception

        Q = sorted(((p, i) for i, p in enumerate(P)))[::-1]
        v0, i0 = Q[0]
        v1, i1 = Q[1]

        tmp = P[:]
        if v0:
            tmp[i0] -= 1
        if v1:
            tmp[i1] -= 1

        tmp1 = P[:]
        if v0:
            tmp1[i0] -= 1

        if check(tmp):
            ans.append(chr(ord('A')+i0) + chr(ord('A')+i1))
            P[i0] -= 1
            P[i1] -= 1
        elif check(tmp1):
            ans.append(chr(ord('A')+i0))
            P[i0] -= 1

    ans = ' '.join(ans)
    print 'Case #%d: %s' % (t, ans)

T = input()
for i in xrange(T):
    solve(i+1)
