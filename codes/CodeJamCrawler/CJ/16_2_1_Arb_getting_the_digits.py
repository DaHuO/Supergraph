#!/usr/bin/env python

import itertools

WORDS = ('ZERO', 'ONE', 'TWO', 'THREE', 'FOUR',
         'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE')


def digit_in_word(word, digit):
  return all(word.count(c) >= digit.count(c) for c in set(digit))


def possible_digits(word):
  digits = []
  for digit in WORDS:
    if digit_in_word(word, digit):
      digits.append(digit)
  return digits


def solve(word):
  for canidates in itertools.permutations(possible_digits(word)):
    canidate = list(word)
    return_value = []
    for each in canidates:
      while digit_in_word(canidate, each):
        try:
          for c in each:
            canidate.remove(c)
        except ValueError:
          continue
        return_value.append(WORDS.index(each))
        if len(canidate) == 0:
          return ''.join(str(c) for c in sorted(return_value))
  print ''.join(canidate)


if __name__ == '__main__':
  number_of_cases = int(raw_input())

  for case in xrange(1, number_of_cases + 1):
    word = str(raw_input())
    print "Case #{0}: {1}".format(case, solve(word))
