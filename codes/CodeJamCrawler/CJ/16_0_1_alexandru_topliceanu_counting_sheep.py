#-*- coding: utf-8 -*-

import os

in_file = '{base}/counting_sheep_small.in'.format(base=os.getcwd())
out_file = '{base}/counting_sheep_small.out'.format(base=os.getcwd())

def has_all_digits(s):
  return s == set(range(10))

def get_digits(num):
  return set([int(i) for i in str(num)])

def count_digits(initial):
  seen_so_far = get_digits(initial)
  previous = initial
  while True:
    current = previous + initial
    if current == previous:
      return 'INSOMNIA'

    seen_so_far = seen_so_far | get_digits(current)
    if has_all_digits(seen_so_far):
      return current

    previous = current

num_tests = 0
tests = []

with open(in_file, 'r') as f:
    num_tests = int(f.readline())
    for __ in range(num_tests):
        tests.append(int(f.readline()))

with open(out_file, 'w') as f:
  for index, initial in enumerate(tests):
    result = count_digits(initial)
    f.write('Case #{index}: {result}{eol}'.format(index=index+1, result=result, eol=os.linesep))
