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
                P = parseTuple(f)
                assert(len(P)==N)
                x = solve(P)
                print>>g, 'Case #%d: %s'  % (n+1,' '.join(c for c in x))
                print 'Case #%d: %s'  % (n+1,' '.join(c for c in x))


import sys, collections
def solve(P):
    bins = []
    for i,c in enumerate(P):
        bins.append([c, chr(ord('A')+i)])
    bins.sort()
    bins.reverse()
    solution = []
    while True:
        bins.sort(reverse=True)
        for i in range(len(bins)-1,-1,-1):
            if bins[i][0] == 0:
                del(bins[i])
        if len(bins) == 0:
            return solution
        if len(bins)==1:
            n,p = bins[0]
            if n%2:
                solution.append(p)
            solution.extend(p+p for i in xrange(n/2))
            return solution
        if len(bins)==3 and bins[0][0] == bins[1][0] == bins[2][0] == 1:
            solution.append(bins[0][1])
            solution.append(bins[1][1]+bins[2][1])
            return solution
        if bins[0][0] > bins[1][0] + 1:
            solution.append(bins[0][1]*2)
            bins[0][0] -= 2
            bins.sort(reverse=True)
            continue
        if bins[0][0] > bins[1][0]:
            if len(bins) == 2:
                solution.append(bins[0][1])
                bins[0][0] -= 1
                continue
        solution.append(bins[0][1]+bins[1][1])
        bins[0][0] -= 1
        bins[1][0] -= 1
        continue

if __name__ == '__main__':
    #main('A-test.in', 'A-test.out')
    #main('A-small-attempt0.in', 'A-small-attempt0.out')
    main('A-large.in', 'A-large.out')
    sys.exit(0)


