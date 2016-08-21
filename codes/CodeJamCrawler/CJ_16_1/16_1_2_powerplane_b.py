#!/usr/bin/env python
import fileinput
import itertools

def solve(matrix):
    d = {}
    missing = set([])
    for row in matrix:
        for ch in row:
            d.setdefault(ch, 0)
            d[ch] = d[ch] + 1
            if d[ch] % 2 == 0:
                missing.discard(ch)
            else:
                missing.add(ch)

    lst = sorted([int(i) for i in missing])
    return ' '.join([str(i) for i in lst])

def process(n, f):
    matrix = []
    for i in xrange(2*n-1):
        matrix.append(next(f).split())
    return solve(matrix)

def main():
    tpl = 'Case #{}: {}'
    case_num =  -1
    f = fileinput.input()
    case_num = int(f.next())

    for num in range(case_num):
        n = int(f.next())
        r = process(n, f)
        print "Case #{}: {}".format(num+1, r)


if __name__ == '__main__':
    main()
