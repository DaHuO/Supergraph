import sys


def solve(n):
    if n == 0:
        return "INSOMNIA"
    x = 0
    seen = set()
    while len(seen) < 10:
        x += n
        seen = seen.union(map(int, str(x)))

    return x


def main():
    lines = map(lambda s: s.strip(), sys.stdin.readlines())
    cases = map(int, lines[1:])
    for i, case in enumerate(cases):
        sol = solve(case)
        print "Case #%d: %s" % (i+1, sol)

if __name__ == '__main__':
    main()
