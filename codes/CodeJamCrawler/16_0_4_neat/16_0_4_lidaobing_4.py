import sys
import random

def foo(ifile):
    k = int(ifile.readline().split()[0])
    return ' '.join([str(x) for x in range(1, k+1)])


def main():
    ifile = sys.stdin
    n = int(ifile.readline())
    for i in range(n):
        print 'Case #%d: %s' % (i+1, foo(ifile))
        sys.stdout.flush()

main()

