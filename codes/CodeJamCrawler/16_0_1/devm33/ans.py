#!/usr/bin/env python


def seen_digits(seen, n):
    for d in str(n):
        seen.add(d)


def solve(n):
    if n == 0:
        return 'INSOMNIA'
    seen = set()
    ten = set([str(d) for d in range(10)])
    cur = n
    seen_digits(seen, cur)
    # print 'solved ' + str(n) + ' to',
    while len(seen) < 10:
        cur += n
        seen_digits(seen, cur)
        # print cur,
        # print '[' + ''.join(sorted(list(ten-seen))) + ']',
    # print 'done.'
    return cur


def main():
    N = int(raw_input())
    for i in range(N):
        print 'Case #%s: %s' % (1+i, solve(int(raw_input())))


if __name__ == "__main__":
    main()
