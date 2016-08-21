#!/usr/bin/python3
# -*- coding: utf-8 -*-
import operator
import functools
from collections import Counter

words = "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"

words_map = {k: str(i) for i, k in enumerate(words)}


def get_unique_letters(words):
    unique_letters = {}
    for letter in functools.reduce(operator.or_, [set(word) for word in words]):
        the_word = None
        for word in words:
            if letter in word and Counter(word)[letter] == 1:
                if the_word:
                    the_word = None
                    break
                the_word = word
        if the_word and the_word not in unique_letters.values():
            unique_letters[letter] = the_word
    return unique_letters

unique_letters_stages = []

rest_words = words

while True:
    unique_letters = get_unique_letters(rest_words)
    unique_letters_stages.append(unique_letters)
    rest_words = set(rest_words) - set(unique_letters.values())
    if not rest_words:
        break


def solve(s):
    cnt = Counter()
    for letter in s:
        cnt[letter] += 1
    numbers = []
    for unique_letters in unique_letters_stages:
        for unique_letter in unique_letters:
            if cnt[unique_letter] > 0:
                word = unique_letters[unique_letter]
                for i in range(cnt[unique_letter]):
                    numbers.append(words_map[word])
                    cnt -= Counter(word)
    return ''.join(sorted(numbers))


if __name__ == '__main__':
    cases_number = int(input())
    for case_number in range(1, cases_number + 1):
        input_args = input()
        print('Case #%s: %s' % (case_number, solve(input_args)))
