# -*- coding: utf-8 -*-


def is_suffix(s, x):
    return s[-len(x):] == x


def solve():
    sn = raw_input()
    n = int(sn)

    if n == 0:
        print 'INSOMNIA'
        return

    flags = [False] * 10
    m = n
    cnt = 1
    while True:
        for e in str(m):
            flags[int(e)] |= True

        if all(flags):
            break

        cnt += 1
        m = cnt * n

    print m


def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        print 'Case #%d:' % i,
        solve()


if __name__ == '__main__':
    main()
