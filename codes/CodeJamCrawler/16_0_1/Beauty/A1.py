import sys
import numpy as np

def solve(n):
  digits = np.zeros(10)
  last_number = 0
  stop = False
  while not stop:
    last_number += n
    for c in str(last_number):
      digits[int(c)] += 1
    stop = len(np.where(digits==0)[0])==0
  return last_number


if __name__ == '__main__':
  f_in = open('A-large.in', 'r')
  f_out = open('out_large.txt', 'w')
  cases = int(f_in.readline())
  for i in xrange(cases):
    n = int(f_in.readline().split()[0])
    if n == 0:
      last_number = "INSOMNIA"
    else:
      last_number = solve(n)
    f_out.write('Case #' + str(i+1) + ": " + str(last_number) + "\n")
