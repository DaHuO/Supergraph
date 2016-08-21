#!/usr/bin/env python3

import sys

BLANK = '-'
HAPPY = '+'

def main():
  fi = sys.stdin
  fo = sys.stdout
  case_count = int(fi.readline().strip())
  for i in range(1, case_count+1):
    pancakes = read_input(fi)
    solution = solve(pancakes)
    display_and_clear(fo, i, solution)

def read_input(f):
  return f.readline().strip()

def display_and_clear(f, i, solution):
  f.write('Case #%d: %d\n' % (i, solution))
  f.flush()

def solve(pancakes):
  blank_runs = find_blank_run_count(pancakes)
  if pancakes[0] == BLANK:
    return (blank_runs - 1) * 2 + 1
  else:
    return blank_runs * 2

def find_blank_run_count(pancakes):
  count = 0
  is_running = False
  
  for pancake in pancakes:
    if pancake == BLANK:
      is_running = True
    else:
      if is_running:
        count += 1
        is_running = False

  if is_running:
    count += 1

  return count

if __name__ == '__main__':
  main()

