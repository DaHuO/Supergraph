import os, sys
import collections as coll
import functools as ft
import itertools as it

class memoize(object):
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)

def get_values(funcs, arg_string):
    return [func(arg) for func, arg in zip(funcs,arg_string.split(" "))]

digits = [
        "ZERO", "ONE", "TWO", "THREE", "FOUR",
        "FIVE", "SIX", "SEVEN", "EIGHT", "NINE",
        ]

digit_pairs = [
("G", "EIGHT"),
("U", "FOUR"),
("W", "TWO"),
("X", "SIX"),
("Z", "ZERO"),
# TWO
("F", "FIVE"),
("H", "THREE"),
("S", "SEVEN"),
# MORE
("O", "ONE"),
("I", "NINE"),
]

case_nums = xrange(1, int(raw_input()) + 1)
for case_num in case_nums:
    found = []
    S = list(raw_input())
    for letter, digit in digit_pairs:
        while letter in S:
            found.append(digits.index(digit))
            for digit_letter in digit:
                S.remove(digit_letter)
    print "Case #%s: %s" % (case_num, ''.join(sorted(map(str,found))))

