#!/usr/bin/env python2

from itertools import izip

def pick_lines(N, lines):
    m = min(l[N] for l in lines)
    return ([l for l in lines if l[N] == m],
            [l for l in lines if l[N] != m])


def sort_lines(N, lines):
    for i in xrange(N):
        pick, lines = pick_lines(i, lines)
        yield pick


def match(a,b):
    for x, y in izip(a,b):
        if x is not None and x != y:
            return False
    return True


def fill(N, lines_list):
    grid = [[None for _ in xrange(N)] for _ in xrange(N)]

    for i, lines in enumerate(lines_list):
        if match(grid[i][:i], lines[0][:i]):
            grid[i] = lines[0][:]
            if len(lines) == 2:
                for j in xrange(N):
                    grid[j][i] = lines[1][j]
        else:
            if len(lines) == 2:
                grid[i] = lines[1][:]
            for j in xrange(N):
                grid[j][i] = lines[0][j]

    return grid


def find_line(N, lines_list, grid):
    for i, lines in enumerate(lines_list):
        if len(lines) == 1:
            if grid[i] == lines[0]:
                return [grid[j][i] for j in xrange(N)]
            else:
                return grid[i]

# def show_grid(grid):
#     print '\n'.join((' '.join(("%3d"%i) for i in line) for line in grid))


def solve():
    N = int(raw_input())

    lines = [map(int,raw_input().split())
             for i in xrange(2*N-1)]

    lines_list = list(sort_lines(N,lines))
    grid = fill(N, lines_list)
    missing = find_line(N, lines_list, grid)
    print ' '.join(map(str,missing))
    # show_grid(grid)


T = int(raw_input())

for i in xrange(1,T+1):
    print 'Case #%d:' % (i),
    solve()
