#! /usr/bin/env python3

digit_to_string = [
    'ZERO',
    'ONE',
    'TWO',
    'THREE',
    'FOUR',
    'FIVE',
    'SIX',
    'SEVEN',
    'EIGHT',
    'NINE'
]

clues = ['Z', 'O', 'W', 'H', 'U', 'V', 'X', 'S', 'G', 'N']

order = [0, 2, 6, 8, 4, 7, 5, 1, 3, 9]


def find_clue(string):
    for digit in order:
        clue = clues[digit]
        if clue in string:
            return digit

def next(string):
    digit = find_clue(string)
    for letter in digit_to_string[digit]:
        string.remove(letter)
    return digit

def find_digits(string):
    digits = []
    while len(string) > 0:
        digit = next(string)
        digits.append(digit)
    return [str(n) for n in sorted(digits)]

T=int(input())
for case in range(1, T+1):
    string = input()
    digits = find_digits(list(string))
    print('Case #%d: %s' % (case, ''.join(digits)))
