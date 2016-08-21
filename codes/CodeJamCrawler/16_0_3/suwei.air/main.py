#!/usr/bin/python

import math

max_num_tested = 2
primes = list([2])

def get_divider(num):
  for x in xrange(2, int(math.floor(math.sqrt(num)))):
    if num % x == 0:
      return x
  return 1

def check(num):
  str_num = bin(num)[2:]
  dividers = dict()

  base2 = num
  dividers[2] = get_divider(base2)
  if dividers[2] == 1:
    return False

  for base in xrange(3, 11):
    target = int(str_num, base)
    dividers[base] = get_divider(target)
    if dividers[base] == 1:
      return False

  print str_num, dividers[2], dividers[3], dividers[4], dividers[5], dividers[6], dividers[7], dividers[8], dividers[9], dividers[10]
  return True

def main():
  line = raw_input()
  T = int(line)
  for t in range(1, T + 1):
    line = raw_input()
    arr = line.split()
    N = int(arr[0])
    J = int(arr[1])
    print 'Case #' + str(t) + ':'
    j = 0
    for n in xrange((1 << (N - 1)) + 1, (1 << N), 2):
      if check(n):
        j += 1
        if j == J:
          return

if __name__ == '__main__':
  main()