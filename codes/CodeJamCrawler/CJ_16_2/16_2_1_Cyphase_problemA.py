from __future__ import print_function

import sys

from collections import Counter

try:
    input = raw_input
except NameError:
    pass


def remove_word(counter, word, times):
    word = word.upper()

    for letter in word:
        counter[letter] -= times


def main():
    num_cases = input()

    for case_idx, s in enumerate(iter(sys.stdin.readline, ''), 1):
        s = s.strip()

        c = Counter(s)
        num_digits = {}

        args = [
            (0, 'ZERO', 'Z'),
            (2, 'TWO', 'W'),
            (4, 'FOUR', 'U'),
            (6, 'SIX', 'X'),
            (8, 'EIGHT', 'G'),
            (1, 'ONE', 'O'),
            (3, 'THREE', 'H'),
            (5, 'FIVE', 'F'),
            (7, 'SEVEN', 'V'),
            (9, 'NINE', 'I'),
        ]

        for num, word, sentinel in args:
            num_digits[num] = c[sentinel]
            remove_word(c, word, c[sentinel])

        num_count_tups = list(sorted(num_digits.items()))

        phone_number = ''.join(str(num) * cnt for num, cnt in num_count_tups)

        print("Case #{}: {}".format(case_idx, phone_number))


if __name__ == '__main__':
    main()
