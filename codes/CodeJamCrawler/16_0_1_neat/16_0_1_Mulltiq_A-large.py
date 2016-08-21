#!/usr/local/env python3.5

import itertools
import sys


def read_numbers(stdin):
    while True:
        current_line = stdin.readline().strip()
        if not current_line:
            break
        yield from (int(x) for x in current_line.split(' '))


def main():
    for _ in itertools.islice(read_numbers(sys.stdin), 1):
        pass
    for i, x in enumerate(read_numbers(sys.stdin)):
        if x == 0:
            print('Case #%s: INSOMNIA' % (i + 1))
            continue
        current = x
        numbers = set(str(x))
        while True:
            if len(numbers) == 10:
                print('Case #%s: %s' % (i + 1, current))
                break
            current += x
            numbers.update(str(current))

if __name__ == '__main__':
    main()
