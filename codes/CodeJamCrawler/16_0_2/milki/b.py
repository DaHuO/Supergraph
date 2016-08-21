def main():
    T = int(raw_input())
    for i in xrange(T):
        S = []
        for c in raw_input().strip():
            if not S or c != S[-1]:
                S.append(c)
        while S and S[-1] == '+':
            S.pop(-1)
        output(i, len(S))

def output(casenum, ret):
    print 'Case #%d: %s' % (casenum+1, ret)


main()
