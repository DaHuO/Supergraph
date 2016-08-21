import sys
import numpy as np

def solve(k, c, s):
  return np.arange(k)+1


if __name__ == '__main__':
  f_in = open('D-small-attempt0.in', 'r')
  f_out = open('out_small.txt', 'w')
  cases = int(f_in.readline())
  for i in xrange(cases):
    k, c, s = f_in.readline().split()
    tiles_pos = solve(int(k), int(c), int(s))
    f_out.write('Case #' + str(i+1) + ":")
    for t in tiles_pos:
      f_out.write(" " + str(t))
    f_out.write("\n")
