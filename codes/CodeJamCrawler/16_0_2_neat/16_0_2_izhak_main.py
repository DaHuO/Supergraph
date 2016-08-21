# -*- coding: utf-8 -*-


def solve(s):
    res = len([sub for sub in s.split("+") if sub]) * 2
    if s.startswith('-'):
        res -= 1
    return res


if __name__ == '__main__':
    f = open("B-large.in", "r")
    t = int(f.readline())
    for i in xrange(1, t + 1):
        s = f.readline().strip()
        r = solve(s)
        print "Case #{}: {}".format(i, r)

