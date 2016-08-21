def parseScalar(f,c=int):
    return c(f.next().strip('\r\n'))
def parseTuple(f,c=int):
    return tuple(c(s) for s in  f.next().strip('\r\n').split())


def main(fn1, fn2):
    with open(fn1) as f:
        with open(fn2, 'w') as g:
            ncases = parseScalar(f)
            for n in range(ncases):
                N = parseScalar(f)
                print N
                x = solve(N)
                print>>g, 'Case #%d: %s'  % (n+1,str(x))
                print 'Case #%d: %s'  % (n+1,str(x)  )


import sys, itertools
def solve(N):
    if N==0:
        return 'INSOMNIA'
    digits = set([])
    for i in itertools.count(1):
        V = i*N
        digits.update(str(V))
        print V, str(sorted(digits))
        if len(digits)==10:
            return V


if __name__ == '__main__':
    #main('A-test.in', 'A-test.out')
    #main('A-small-attempt0.in', 'A-small-attempt0.out')
    main('A-large.in', 'A-large.out')
    sys.exit(0)


