# -*- coding: utf-8 -*-

def solve():
    k, c, s = map(int, raw_input().split())
    print ' '.join(map(str, range(1, s + 1)))


def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        print 'Case #%d:' % i,
        solve()


if __name__ == '__main__':
    main()
