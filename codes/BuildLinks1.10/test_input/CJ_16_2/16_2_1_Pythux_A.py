from __future__ import print_function
import sys
from collections import Counter

NUMBERS = {
    9: "NINE"
}


def main():
    t = int(raw_input())
    for i in range(t):
        s = raw_input()
        letters = Counter(s)
        result = []

        # Count 0
        if 'Z' in letters:
            result.extend('0' * letters['Z'])
            letters.subtract('ZERO' * letters['Z'])
        if 'W' in letters:
            result.extend('2' * letters['W'])
            letters.subtract('TWO' * letters['W'])
        if 'X' in letters:
            result.extend('6' * letters['X'])
            letters.subtract('SIX' * letters['X'])
        if 'G' in letters:
            result.extend('8' * letters['G'])
            letters.subtract('EIGHT' * letters['G'])
        if 'H' in letters:
            result.extend('3' * letters['H'])
            letters.subtract('THREE' * letters['H'])
        if 'U' in letters:
            result.extend('4' * letters['U'])
            letters.subtract('FOUR' * letters['U'])
        if 'F' in letters:
            result.extend('5' * letters['F'])
            letters.subtract('FIVE' * letters['F'])
        if 'O' in letters:
            result.extend('1' * letters['O'])
            letters.subtract('ONE' * letters['O'])
        if 'V' in letters:
            result.extend('7' * letters['V'])
            letters.subtract('SEVEN' * letters['V'])
        if 'I' in letters:
            result.extend('9' * letters['I'])
            letters.subtract('NINE' * letters['I'])
        print("Case #%s: %s" % (i + 1, ''.join(sorted(result))))




main()
