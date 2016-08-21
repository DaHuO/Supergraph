#!/usr/bin/python
import sys

# Part of 2016 Google code jam


def find_word(word):
    last_word = ''
    chars = list(word)

    for char in chars:
        if last_word == '':
            last_word = char
        elif char < last_word[0]:
            last_word = last_word + char
        else:
            last_word = char + last_word

    return last_word


T = int(raw_input().strip())

for i in range(1, T+1):
    w = raw_input().strip()
    result = find_word(w)
    print 'Case #' + str(i) + ': ' + str(result)
