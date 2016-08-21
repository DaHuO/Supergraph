def parseScalar(f,c=int):
    return c(f.next().strip('\r\n'))
def parseTuple(f,c=int):
    return tuple(c(s) for s in  f.next().strip('\r\n').split())


def main(fn1, fn2):
    with open(fn1) as f:
        with open(fn2, 'w') as g:
            ncases = parseScalar(f)
            for n in range(ncases):
                K,C,S = parseTuple(f)
                print K,C,S
                x = solve(K,C,S)
                print>>g, 'Case #%d: %s'  % (n+1, x)
                print 'Case #%d: %s'  % (n+1, x)



import sys
def solve(K,C,S):
    if K == 1:
        return '1'
    if S >= K-1 and C >= 2:
        return ' '.join(str(i) for i in range(2,K+1))
    elif S == K and C == 1:
        return ' '.join(str(i) for i in range(1,K+1))
    else:
        return 'IMPOSSIBLE'

if __name__ == '__main__':
    main('D-test.in', 'D-test.out')
    main('D-small-attempt0.in', 'D-small-attempt0.out')
    #main('D-large.in', 'D-large.out')
    sys.exit(0)


