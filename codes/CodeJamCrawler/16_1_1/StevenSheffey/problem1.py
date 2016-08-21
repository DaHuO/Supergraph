#!/bin/python3
import sys

words = map(str.rstrip, sys.stdin.readlines()[1:])

for index, word in enumerate(words):
    last_word = [word[0]]
    for letter in word[1:]:
        if letter < last_word[0]:
            last_word.append(letter)
        else:
            last_word.insert(0, letter)
    print('Case #{}: {}'.format(index+1, ''.join(last_word)))
