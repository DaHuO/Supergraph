from __future__ import division, print_function

import itertools
import sys


POSITIVE_PANCAKE = '+'
NEGATIVE_PANCAKE = '-'
PANCAKES_MAP = {
    POSITIVE_PANCAKE: NEGATIVE_PANCAKE,
    NEGATIVE_PANCAKE: POSITIVE_PANCAKE,
}


def are_all_pancakes_happy(pancakes):
    return all(pancake == POSITIVE_PANCAKE for pancake in pancakes)


def flip(pancakes, n):
    return (
        ''.join(PANCAKES_MAP[pancake] for pancake in pancakes[:n]) +
        pancakes[n:]
    )


def solve():
    pancakes = read()
    flips = 0
    while not are_all_pancakes_happy(pancakes):
        negative_pancake_index = pancakes.rfind(NEGATIVE_PANCAKE)
        pancakes = flip(pancakes, negative_pancake_index + 1)
        flips += 1
    return flips


def main():
    """Main."""
    n = read_int()
    for i in xrange(1, n + 1):
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
