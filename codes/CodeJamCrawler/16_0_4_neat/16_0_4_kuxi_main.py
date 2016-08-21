import sys


def solve(k, c, s):
    return " ".join(map(str, range(1, k+1)))


def main():
    lines = map(lambda s: s.strip(), sys.stdin.readlines())
    cases = map(lambda line: map(int, line.split()), lines[1:])
    for i, case in enumerate(cases):
        sol = solve(*case)
        print "Case #%d: %s" % (i+1, sol)

if __name__ == '__main__':
    main()
