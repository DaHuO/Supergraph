#!/usr/bin/env python3

import sys


ALL_DIGITS = frozenset((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))


def solve(n):
  if n == 0:
    return "INSOMNIA"
  digits_seen = set()
  i = 1
  while digits_seen != ALL_DIGITS:
    v = n * i
    digits = set(map(int, str(v)))
    for d in digits:
      digits_seen.add(d)
    i += 1
  return str(v)

if __name__ == "__main__":
  input_filepath = sys.argv[1]

  with open(input_filepath, "rt") as input_file:
    T = int(next(input_file))

    for i in range(1, T + 1):
      n = int(next(input_file))
      print("Case #%u: %s" % (i, solve(n)))

    assert(i == T)
