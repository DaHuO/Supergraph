from sys import stdin

def flip(s):
    return ''.join([{'-' : '+', '+' : '-'}[x] for x in s])

def f(s):
    if s == '-':
        return 1
    if s == '+':
        return 0
    if s[-1] == '+':
        return f(s[:-1])
    return 1 + f(flip(s[:-1]))

for t in range(1, int(stdin.readline()) + 1):
    print 'Case #%d: %d' % (t, f(stdin.readline().strip()))
