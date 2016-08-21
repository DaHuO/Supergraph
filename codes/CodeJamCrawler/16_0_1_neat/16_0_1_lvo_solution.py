#!/usr/bin/env python3
import sys


def doit(initial_value_str):
    '''
    >>> doit('0')
    'INSOMNIA'
    >>> doit('1')
    '10'
    >>> doit('2')
    '90'
    >>> doit('11')
    '110'
    >>> doit('1692')
    '5076'
    '''
    initial_value_int = value = int(initial_value_str)
    digits = set()
    for _ in range(1000):
        result = str(value)
        digits.update(result)
        if len(digits) == 10:
            return result
        value += initial_value_int
    return 'INSOMNIA'


def main():
    line_count = int(sys.stdin.readline().strip())
    for case_no in range(1, line_count + 1):
        value_str = sys.stdin.readline().strip()
        result = doit(value_str)
        sys.stdout.write('Case #{}: {}\n'.format(case_no, result))


if __name__ == '__main__':
    main()
