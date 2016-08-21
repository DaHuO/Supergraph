def is_majority(P):
    s = sum(P)
    for p in P:
        if p > s / 2.0:
            return True

    return False

def solution(P):
    ans = ''
    while sum(P) > 0:
        curAns = ''
        f = False
        for i in range(len(P)):
            if f: break
            for j in range(i, len(P)):
                nP = P[:]
                nP[i] -= 1
                nP[j] -= 1
                if not is_majority(nP):
                    curAns += chr(i + ord('A')) + chr(j + ord('A'))
                    P[i] -= 1
                    P[j] -= 1
                    f = True
                    break
        if not f:
            for i in range(len(P)):
                nP = P[:]
                nP[i] -= 1
                if not is_majority(nP):
                    curAns += chr(i + ord('A'))
                    P[i] -= 1
                    break
        ans += curAns + ' '
    return ans


T = int(raw_input())
for i in xrange(T):
    N = int(raw_input())
    P = map(int, raw_input().split())
    print 'Case #%d: %s' % (i+1, solution(P))
