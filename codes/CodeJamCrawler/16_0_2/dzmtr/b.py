import sys

T = int(sys.stdin.readline())
for t in xrange(1, T + 1):
    s = list(sys.stdin.readline()[:-1])
    i = len(s) - 1
    while i >= 0 and s[i] == '+':
        i -= 1
    if i == -1:
        x = 0
    else:
        del s[i + 1:]
        x = 1
        for i in xrange(1, len(s)):
            if s[i] != s[i - 1]:
                x += 1
    sys.stdout.write('Case #%d: %d\n' % (t, x))
