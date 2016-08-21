from __future__ import division, print_function

import itertools
import string
import sys


def solve():
    n = read_int()
    ps = read_int_array()
    ns = string.ascii_uppercase
    es = []
    p = sum(ps)
    while p:
        if n == 2:
            j = max(ps)
            if ps.count(j) == 2 and all((x == 0 or x == j) for x in ps):
                jj = j
                while jj:
                    j1 = ps.index(j)
                    j2 = ps.index(j, j1 + 1)
                    es.append(ns[j1] + ns[j2])
                    jj -= 1
                return ' '.join(es)
        #
        i = max(ps)
        assert i * 2 <= sum(ps), ps
        #
        m = max(ps)
        i = ps.index(m)
        es.append(ns[i])
        ps[i] -= 1
        if ps[i] == 0:
            n -= 1
        p -= 1
    return ' '.join(es)


def main():
    for i in xrange(1, read_int() + 1):
        write('Case #{}: {}'.format(i, solve()))


def bye(message=None):
    if message is not None:
        write(message)
    sys.exit()


def times(n):
    return itertools.repeat(None, n)


def read(func=None):
    a = sys.stdin.readline().rstrip('\n')
    return a if func is None else func(a)


def read_array(func=None, sep=None, max_split=-1):
    array = read().split(sep, max_split) if sep != '' else list(read())
    return array if func is None else [func(a) for a in array]


def read_2d_array(n, func=None, sep=None, max_split=-1):
    return [read_array(func, sep, max_split) for _ in times(n)]


def read_int():
    """:rtype: int"""
    return read(int)


def read_int_array(sep=None, max_split=-1):
    """:rtype: list[int]"""
    return read_array(int, sep, max_split)


def read_int_2d_array(n, sep=None, max_split=-1):
    """:rtype: list[list[int]]"""
    return read_2d_array(n, int, sep, max_split)


def write(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    sys.stdout.write(sep.join(str(a) for a in args) + end)


def write_array(array, **kwargs):
    write(*array, **kwargs)


def write_2d_array(array, **kwargs):
    [write_array(a, **kwargs) for a in array]


def _main_():
    name = ''
    names = ''
    if name or names:
        in_name = name + '.in' if name else 'input.txt'
        out_name = name + '.out' if name else 'output.txt'
        stdin = sys.stdin
        stdout = sys.stdout
        sys.stdin = open(in_name)
        sys.stdout = open(out_name, 'w')
        main()
        sys.stdin.close()
        sys.stdout.close()
        sys.stdin = stdin
        sys.stdout = stdout
    else:
        main()


_main_()
