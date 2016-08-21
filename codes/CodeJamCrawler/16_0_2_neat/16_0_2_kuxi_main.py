import sys


def solve(case, target='+'):
    if target == '+':
        other = '-'
    else:
        other = '+'
    if case == target:
        return 0
    if case == other:
        return 1
    if case[-1] == target:
        return solve(case[:-1], target)
    return 1 + solve(case[:-1], other)


def main():
    cases = map(lambda s: s.strip(), sys.stdin.readlines()[1:])
    for i, case in enumerate(cases):
        ans = solve(case)
        print "Case #%d: %s" % (i+1, ans)


if __name__ == '__main__':
    main()
