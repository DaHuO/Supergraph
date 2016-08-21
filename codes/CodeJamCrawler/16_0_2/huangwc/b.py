import sys

sys.stdin = open('B-large.in', 'r')
sys.stdout = open('B-large.out', 'w')

for c in range(1, int(input()) + 1):

    last = ''
    s = ''

    for x in input().strip():
        if x != last:
            s += x
        last = x

    n = len(s) if s[-1] == '-' else len(s) - 1

    print('Case #%s: %s' % (c, n))
