
import sys

def solve(A, N):
    if N == 1: return list(A[0])
    A.sort(key=lambda x: x[0])
    if A[1][0] == A[0][0]:
        st = [x for x in A[0][1:]] + [x for x in A[1][1:]]
        for x in A[2:]:
            del st[st.index(x[0])]
        B = [x[1:] for x in A[2:]]
        return st + solve(B, N - 1)
    else:
        st = set(x for x in A[0][1:])
        B = []
        for x in A[1:]:
            if x[0] in st:
                st.discard(x[0])
            else:
                B.append(x)
        return [A[0][0]] + [x[0] for x in B]

line = lambda: sys.stdin.readline()
T = int(line())
for i in xrange(T):
    N = int(line())
    A = []
    for j in xrange(2 * N - 1):
        a = map(int, line().split(' '))
        A.append(tuple(a))
    R = solve(A, N)
    print "Case #%d: %s" % (i + 1, ' '.join(map(str, R)))
