#!/usr/bin/env python3
import sys


def main():
    count = int(next(sys.stdin).rstrip())
    for i in range(1, count + 1):
        src = next(sys.stdin).rstrip()
        old_c, old_j = src.split()
        c, j = solve(old_c, old_j)
        sys.stdout.write('Case #{}: {} {}\n'.format(i, c, j))


def solve(src1, src2):
    '''
    >>> solve('1?', '2?')
    ('19', '20')
    >>> solve('?2?', '??3')
    ('023', '023')
    >>> solve('?', '?')
    ('0', '0')
    >>> solve('?5', '?0')
    ('05', '00')
    >>> solve('?8', '93')
    ('88', '93')
    '''
    assert len(src1) == len(src2)
    return min(
        combinations(src1, src2),
        key=lambda x: (
            abs(int(x[0]) - int(x[1])),
            int(x[0]),
            int(x[1]),
        ),
    )


def combinations(src1, src2):
    if not src1:
        yield '', ''
    elif src1[0] == '?':
        if src2[0] == '?':
            for c1 in '0123456789':
                for c2 in '0123456789':
                    for sub1, sub2 in combinations(src1[1:], src2[1:]):
                        yield c1 + sub1, c2 + sub2
        else:
            c = src2[0]
            for i in '0123456789':
                for sub1, sub2 in combinations(src1[1:], src2[1:]):
                    yield i + sub1, c + sub2
    elif src2[0] == '?':
        for y, x in combinations(src2, src1):
            yield x, y
    else:
        for sub1, sub2 in combinations(src1[1:], src2[1:]):
            yield src1[0] + sub1, src2[0] + sub2


if __name__ == '__main__':
    main()
