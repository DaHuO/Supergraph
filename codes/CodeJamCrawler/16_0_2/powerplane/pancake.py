#!/usr/bin/env python
import fileinput
import sys

def main():
    out_tpl = 'Case #{}: {}'
    case_num = -1
    if len(sys.argv) >= 2:
        fname = sys.argv[1]
    else:
        fname = None

    for idx, line in enumerate(fileinput.input(fname)):
        if idx == 0:
            case_num = int(line.strip())
        else:
            num, visited = search(list(line.strip()))
            print out_tpl.format(idx, num)


def inv(i):
    return '+' if i == '-' else '-'

def flip(seq, n):
    return [inv(i) for i in reversed(seq[:n])] + seq[n:]

def search(src_seq):
    visited = {}
    length = len(src_seq)
    depth = 0
    expecting = len(src_seq) * '+'

    if expecting == ''.join(src_seq):
        return depth, visited

    frontiers = []
    to_visit = [src_seq]

    while to_visit:
        frontiers = to_visit
        to_visit = []
        depth += 1
        for s in frontiers:
            for j in xrange(1, length+1):
                s2 = flip(s, j)
                k = ''.join(s2)

                if k not in visited:
                    visited[k] = (''.join(s), depth)
                    to_visit.append(s2)

                if k == expecting:
                    return depth, visited
    return -1, visited

if __name__ == '__main__':
    main()
