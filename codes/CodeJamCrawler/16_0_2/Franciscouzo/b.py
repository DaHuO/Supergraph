def flip(s, i):
    out = []
    for c in reversed(s[:i]):
        if c == '+':
            out.append('-')
        else:
            out.append('+')
    return ''.join(out) + s[i:]

def solve(s):
    steps = 0
    while s != '+' * len(s):
        steps += 1
        i = len(s) - len(s.lstrip(s[0]))
        s = flip(s, i)
    return steps

cases = int(raw_input())
for case in xrange(1, cases + 1):
    s = raw_input()
    print 'Case #{}: {}'.format(case, solve(s))
