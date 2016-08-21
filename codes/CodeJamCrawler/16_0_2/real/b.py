import sys, itertools, collections
sys.setrecursionlimit(10000)

read_ints = lambda: map(int, raw_input().split())
read_int  = input


def flip(c):
    return '+' if c == '-' else '-'


for no_t in xrange(1, read_int() + 1):
    s = raw_input()
    ans = 0
    while s and s[-1] == '+':
        s = s[:-1]

    last = '?'
    for cur in s:
        if last != cur:
            last = cur
            ans += 1

    print 'Case #%d: %s' % (no_t, ans)
