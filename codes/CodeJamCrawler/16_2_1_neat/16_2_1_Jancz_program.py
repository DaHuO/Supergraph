#!/usr/bin/env python

from sys import argv

all_words = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']


def find_words(v):
    possible_words = []
    for number in all_words:
        found_all = True
        for current_character in number:
            if current_character not in v:
                found_all = False
        if found_all:
            possible_words.append(number)
    return possible_words


def remove_from_string(v, word):
    for c in word:
        v = v.replace(c, '', 1)
    return v


def convert_to_int(word):
    return all_words.index(word)


def find_numbers_of_text(v):
    possible_words = find_words(v)
    for word in possible_words:
        new_v = remove_from_string(v, word)
        if len(new_v) == 0:
            return True, [convert_to_int(word)]
        else:
            is_successful, result = find_numbers_of_text(new_v)
            if is_successful:
                result.append(convert_to_int(word))
                return True, result
    return False, [-1]


def solve(v):
    is_successful, result = find_numbers_of_text(v)
    if is_successful:
        result = sorted(result)
        result = [str(i) for i in result]
        return ''.join(result)
    return 'ERROR'


input_file = open(argv[1], 'r')
number_of_cases = int(input_file.readline())
for current_case_number in range(1, number_of_cases + 1):
    input_text = input_file.readline().strip()
    print('Case #%i: %s' % (current_case_number, solve(input_text)))
