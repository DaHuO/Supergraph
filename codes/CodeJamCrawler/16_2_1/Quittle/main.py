import itertools
import math
import sys

NUMBERS = [ 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE' ]

def main():
    num_cases = int(sys.stdin.readline())

    line_num = 1
    for line in sys.stdin:
        line = line.strip()

        solution = compute(line, 0)
        assert len(solution) == 1
        assert_is_numeric_list(solution[0])
        string_solution = ''.join(str(i) for i in solution[0])
        assert_is_string(string_solution)

        print 'Case #%d: %s' % (line_num, string_solution)

        line_num += 1

    assert num_cases == line_num - 1


def assert_is_numeric(n):
    assert type(n) in [int, long]


def assert_is_string(s):
    assert isinstance(s, basestring)


def assert_is_numeric_list(arr):
    for n in arr:
        assert_is_numeric(n)


def assert_is_bool_list(arr):
    for b in arr:
        assert type(b) is bool


def test():
    pass


def compute(scrambled_number, min_value):
    ''' Converts scrambled text into a phone number '''

    if not scrambled_number:
        return [[]]

    possibilities = []
    for i, number in enumerate(counted_numbers()[min_value:], min_value):
        valid_number = True
        for letter in number:
            if scrambled_number.count(letter) < number[letter]:
                valid_number = False
                break
        if not valid_number:
            continue
        reduced_scrambled_number = scrambled_number
        for letter in number:
            reduced_scrambled_number = reduced_scrambled_number.replace(letter, '', number[letter])

        for possibility in compute(reduced_scrambled_number, i):
            possibilities.append([i] + possibility)

    return possibilities


def sorted_numbers():
    return [''.join(sorted(number)) for number in NUMBERS ]

def counted_numbers():
    ret = []
    for number in NUMBERS:
        counts = {}
        for letter in number:
            counts[letter] = number.count(letter)
        ret.append(counts)
    return ret


if __name__ == '__main__':
    test()
    #print 'All tests passed'
    main()