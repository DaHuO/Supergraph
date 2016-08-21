import sys


outf = None
inf = None


def solve(N):
    seen = set()
    i = 0
    if N == 0:
        return 0, 'INSOMNIA'
    for i in range(1, 10000):
        n = str(i * N)
        for d in str(n):
            seen.add(d) 
        if len(seen) == 10:
            return i, n
    raise Exception('Unexpected insomnia for number %d' % i)


def solve_file():
    lines = list(inf)
    assert int(lines[0].strip()), len(lines[1:])
    for i, case in enumerate(lines[1:], 1):
        N = int(case.strip())
        result = solve(N)[1]
        print >> outf, 'Case #%d: %s' % (i, result)


if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = infile.replace('.in', '') + '.out'
    with open(infile) as inf, open(outfile, 'w') as outf:
        solve_file()
