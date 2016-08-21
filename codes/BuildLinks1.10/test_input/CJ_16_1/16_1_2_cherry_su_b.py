def solve(N, grid):
    tally = [0]*2501
    for l in grid:
        for x in l:
            tally[x] += 1
    buf = []
    for i, e in enumerate(tally):
        if e % 2 == 1:
            buf.append(i)
    missing = sorted(buf)
    return ' '.join(map(str, buf))

if '__main__' == __name__:
    T = int(raw_input())
    for _t in range(T):
        grid = []
        N = int(raw_input())
        for _ in range(2*N-1):
            buf = map(int, raw_input().strip().split())
            grid.append(buf)
        print "Case #%d: %s" % (_t+1, solve(N, grid))
