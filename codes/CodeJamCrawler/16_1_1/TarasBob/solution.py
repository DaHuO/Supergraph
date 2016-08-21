#!/usr/bin/python
from sys import stdin, stderr

def find_largest_last(letters, start, end):
  cur = 'A'
  result = -1
  for i in xrange(start, end):
    if letters[i] >= cur:
      cur = letters[i]
      result = i
  return result

def solve(letters):
  result = ''
  start = 0
  end = len(letters)
  arr = []
  while True:
    ll = find_largest_last(letters, 0, end)
    if ll == -1:
      break
    arr.append((letters[ll], letters[ll+1:end]))
    end = ll
  for i in xrange(len(arr) - 1, -1, -1):
    result = arr[i][0] + result + arr[i][1]
  return result

num_cases = int(stdin.readline())
for case_num in range(num_cases):
  letters = stdin.readline().strip()
  result = 'Case #{0}: {1}'.format(case_num + 1, solve(letters))
  print result
  print >>stderr, result
