import sys


def solve(s, sign):

    actions = 0

    if s:
        if s[-1] == sign:
            actions = solve(s[:-1], '+' if sign == '+' else '-')
        else:
            actions = solve(s[:-1], '+' if sign == '-' else '-') + 1

    return actions


T = int(sys.stdin.next())

for i in range(T):
    s = sys.stdin.next().strip()
    print('Case #%i: %i' % (i + 1, solve(s, '+')))
