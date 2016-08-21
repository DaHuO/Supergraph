import sys
import random

cache = {}

def revert(a, n):
    na = len(a)
    res = [0] * na
    for i in range(na):
        if i + n >= na:
            res[i] = 1 - a[i]
        else:
            res[i] = a[i]
    return res

def foo4(a):
    if len(a) == 0:
        return 0
    if a[0]:
        return foo3(a[1:])
    na = len(a)
    res = 100000
    if not a[-1]:
        res = min(res, foo3(revert(a, na))+1)
    for i in range(1, na):
        a2 = revert(a, i)
        if not a2[-1]:
            res = min(res, foo3(revert(a2, na))+2)
    return res

def foo3(a):
    a2 = tuple(a)
    if a2 not in cache:
        cache[a2] = foo4(a)
    return cache[a2]




def foo(ifile):
    a = [int(x == '+') for x in ifile.readline().strip()][::-1]
    return foo3(a)

def main():
    ifile = sys.stdin
    n = int(ifile.readline())
    for i in range(n):
        print 'Case #%d: %s' % (i+1, foo(ifile))
        sys.stdout.flush()

main()

