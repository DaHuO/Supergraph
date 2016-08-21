#!/usr/bin/env python2.7

import sys


def challenge(initial):
    """
    :type initial: str
    :rtype: str
    """
    result = dict()
    letter_map = dict()
    for letter in initial:
        count = letter_map.get(letter, 0) + 1
        letter_map[letter] = count

    # Zero
    zeroes = letter_map.get('Z', 0)
    decrease(letter_map, 'ZERO', zeroes)

    # tWo
    twos = letter_map.get('W', 0)
    decrease(letter_map, 'TWO', twos)

    # foUr
    fours = letter_map.get('U', 0)
    decrease(letter_map, 'FOUR', fours)

    # siX
    sixes = letter_map.get('X', 0)
    decrease(letter_map, 'SIX', sixes)

    # Seven
    sevens = letter_map.get('S', 0)
    decrease(letter_map, 'SEVEN', sevens)

    # eiGht
    eights = letter_map.get('G', 0)
    decrease(letter_map, 'EIGHT', eights)

    # One
    ones = letter_map.get('O', 0)
    decrease(letter_map, 'ONE', ones)

    # Three
    threes = letter_map.get('T', 0)
    decrease(letter_map, 'THREE', threes)

    # Five
    fives = letter_map.get('F', 0)
    decrease(letter_map, 'FIVE', fives)

    # nIne
    nines = letter_map.get('I', 0)
    decrease(letter_map, 'NINE', nines)

    # Validate
    for (key, value) in letter_map.items():
        if value != 0:
            print 'ERROR: %s = %d for CASE %s' % (key, value, initial)

    return "%s%s%s%s%s%s%s%s%s%s" % (
        ('0' * zeroes),
        ('1' * ones),
        ('2' * twos),
        ('3' * threes),
        ('4' * fours),
        ('5' * fives),
        ('6' * sixes),
        ('7' * sevens),
        ('8' * eights),
        ('9' * nines)
    )


def decrease(map, word, value):
    """
    :type map: dict[str, int]
    :type key: str
    :type value: int
    """
    for letter in word:
        if map.has_key(letter):
            map[letter] -= value
        else:
            map[letter] = 0


def main(stream):
    """
    :type stream: file
    """
    first_line = stream.readline()
    case_count = int(first_line)
    for (case_number, line) in enumerate(stream, start=1):
        n = line.strip()
        result = challenge(n)
        print 'Case #%(case_number)d: %(result)s' % dict(
            case_number=case_number,
            result=result
        )
        if case_number == case_count:
            break


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        with open(file_name) as file_stream:
            main(file_stream)
    else:
        main(sys.stdin)
