#!/usr/bin/env python3

import sys
from operator import itemgetter

def main():
  fi = sys.stdin
  fo = sys.stdout
  case_count = int(fi.readline().strip())
  for i in range(1, case_count+1):
    n, ps = read_input(fi)
    solution = solve(n, ps)
    display_and_clear(fo, i, solution)

def read_input(f):
  n = int(f.readline().strip())
  ps = [int(token) for token in f.readline().split()]
  return n, ps

def display_and_clear(f, i, solution):
  f.write('Case #%d: %s\n' % (i, solution))
  f.flush()

def solve(n, ps):
  plan = []
  party_count = n
  while sum(ps) > 0:
    cur_step = []
    ind1, ind2 = find_max_two_indices(ps)

    if party_count > 2:
      party_count = reduce(party_count, ps, cur_step)
    elif party_count == 2 and ind1[1] != ind2[1]:
      party_count = reduce(party_count, ps, cur_step)
    else:
      party_count = reduce(party_count, ps, cur_step)
      party_count = reduce(party_count, ps, cur_step)

    plan.append(''.join(cur_step))
  return ' '.join(plan)

def reduce(party_count, ps, cur_step):
    mi1, mv1 = find_max_index(ps)
    if mv1 > 0:
      p1 = get_party(mi1)
      cur_step.append(p1)
      ps[mi1] -= 1
      if ps[mi1] == 0:
        party_count -= 1

    return party_count

def find_max_index(ps):
  return max(enumerate(ps), key=itemgetter(1))

def find_max_two_indices(ps):
  return sorted(enumerate(ps), key=itemgetter(1), reverse=True)[:2]

def get_party(index):
  return chr(ord('A') + index)

if __name__ == '__main__':
  main()

