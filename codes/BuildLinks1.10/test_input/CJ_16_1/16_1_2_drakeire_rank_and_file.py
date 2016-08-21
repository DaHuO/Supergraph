#!/usr/bin/env python3

import sys
from copy import deepcopy

def main():
  fi = sys.stdin
  fo = sys.stdout
  case_count = int(fi.readline().strip())
  for i in range(1, case_count+1):
    n, lists = read_input(fi)
    solution = solve(n, lists)
    display_and_clear(fo, i, solution)

def read_input(f):
  n = int(f.readline().strip())
  lists = []
  for i in range(2*n - 1):
    lists.append([int(token) for token in f.readline().split()])
  return n, lists

def display_and_clear(f, i, solution):
  sol_str = ' '.join([str(elt) for elt in solution])
  f.write('Case #%d: %s\n' % (i, sol_str))
  f.flush()

def solve(n, lists):
  lists = sorted(lists)
  cur_indices = []
  useds = [False] * len(lists)
  elt_set = set()
  for li in lists:
    elt_set |= set(li)

  solutions = []
  bt(cur_indices, useds, lists, n, elt_set, solutions)
  remaining = None
  for solution in solutions:
    try:
      remaining = find_remaining(lists, solution, n)
    except:
      pass
  return remaining

def find_remaining(lists, solution, n):
  grid = []
  for index in solution:
    grid.append(lists[index])

  cols = []
  for i in range(n):
    cols.append([grid[j][i] for j in range(n)])

  solution_set = set(solution)
  for i in range(2*n - 1):
    if i not in solution_set:
      '''
      print(cols)
      print(lists[i])
      print(i)
      print(solution_set)
      '''
      cols.remove(lists[i])

  return cols[0]

def bt(cur_indices, useds, lists, n, elt_set, solutions):
  #if solutions:
  #  return

  if len(cur_indices) == n:
    cur_set = set()
    for li_index in cur_indices:
      cur_set |= set(lists[li_index])
    if cur_set == elt_set:
      solutions.append(deepcopy(cur_indices))
    return 

  for i in range(len(lists)):
    if useds[i]:
      continue

    if cur_indices \
        and not can_follow(lists[cur_indices[-1]], lists[i]):
      continue

    useds[i] = True
    cur_indices.append(i)

    bt(cur_indices, useds, lists, n, elt_set, solutions)

    cur_indices.pop()
    useds[i] = False

def can_follow(l1, l2):
  for n1, n2 in zip(l1, l2):
    if n1 >= n2:
      return False

  return True

if __name__ == '__main__':
  main()

