from __future__ import division, print_function

import itertools
import sys


def generate_possible_jamcoins(length):
    length -= 2
    for i in xrange(2 ** length):
        yield '1' + bin(i)[2:].rjust(length, '0') + '1'


def get_number_from_jamcoin(possible_jamcoin, base):
    return int(possible_jamcoin, base)


def get_divisor(number):
    if number % 2 == 0:
        return 2
    for i in xrange(3, int(number ** .5) + 2, 2):
        if number % i == 0:
            return i
    return 0


def check_legitimation_of_jamcoin(possible_jamcoin):
    divisors = []
    for base in xrange(2, 11):
        number = get_number_from_jamcoin(possible_jamcoin, base)
        divisor = get_divisor(number)
        if divisor == 0:
            return []
        divisors.append(divisor)
    return divisors


def solve():
    length, jamcoins_number = read_int_array()
    for possible_jamcoin in generate_possible_jamcoins(length):
        divisors = check_legitimation_of_jamcoin(possible_jamcoin)
        if divisors:
            write_array(possible_jamcoin, sep='', end=' ')
            write_array(divisors, sep=' ')
            jamcoins_number -= 1
            if jamcoins_number == 0:
                break


def main():
    """Main."""
    n = read_int()
    for i in xrange(1, n + 1):
        write('Case #{}:'.format(i))
        solve()


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
