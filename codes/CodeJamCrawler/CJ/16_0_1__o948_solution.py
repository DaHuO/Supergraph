import sys

def readline():
    return sys.stdin.readline().rstrip()

def f(n):
    was = set()
    k = n
    for _ in xrange(1000):
        was.update(str(k))
        if len(was) == 10:
            return k
        k += n
    return -1

def solve():
    t = int(readline())
    for i in xrange(1, t+1):
        n = int(readline())

        print 'Case #%d:' % i,
        n = f(n)
        if n == -1:
            print 'INSOMNIA'
        else:
            print n

if __name__ == '__main__':
    solve()

