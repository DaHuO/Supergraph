import sys, itertools, collections
sys.setrecursionlimit(10000)

read_ints = lambda: map(int, raw_input().split())
read_int  = input


def gao(n):
    if n == 0:
        return 'INSOMNIA'
    a = 0
    s = set()
    while len(s) < 10:
        a += n
        s = s.union(list(str(a)))

    return a


for no_t in xrange(1, read_int() + 1):
    n = read_int()
    print 'Case #%d: %s' % (no_t, gao(n))
