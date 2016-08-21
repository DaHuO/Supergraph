#!/usr/bin/env python3
import sys

from collections import Counter


def main():
    count = int(next(sys.stdin).rstrip())
    for i in range(1, count + 1):
        src = next(sys.stdin).rstrip()
        sys.stdout.write('Case #{}: {}\n'.format(i, solve(src)))


DIGITS = [
    Counter("ZERO"),
    Counter("ONE"),
    Counter("TWO"),
    Counter("THREE"),
    Counter("FOUR"),
    Counter("FIVE"),
    Counter("SIX"),
    Counter("SEVEN"),
    Counter("EIGHT"),
    Counter("NINE"),
]


def solve(src):
    '''
    >>> solve('OZONETOWER')
    '012'
    >>> solve('WEIGHFOXTOURIST')
    '2468'
    >>> solve('OURNEONFOE')
    '114'
    >>> solve('ETHER')
    '3'
    '''
    result = subsolve(Counter(src))
    return ''.join(map(str, result))


def subsolve(src_letters):
    if not src_letters:
        return ()
    for digit, digit_letters in enumerate(DIGITS):
        if all(src_letters[letter] >= count for letter, count in digit_letters.items()):
            result = subsolve(src_letters - digit_letters)
            if result is not None:
                return (digit, ) + result
    return None

if __name__ == '__main__':
    main()
