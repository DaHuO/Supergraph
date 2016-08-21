import sys


def revenge_pancakes(s):
    if '-' not in s:
        return 0
    if '+' not in s:
        return 1

    flips = 0
    i = 1
    cur = s[0]
    while i < len(s):
        if s[i] != cur:
            flips += 1
            cur = '-' if cur == '+' else '+'
        i += 1
    if cur == '-':
        flips += 1
    return flips

num_tests = int(sys.stdin.readline().strip())
for i in range(num_tests):
    s = sys.stdin.readline().strip()
    print 'Case #%d:' % (i+1), revenge_pancakes(s)
